# Deep Research & Intelligence: Veritasium XZ Supply Chain Attack (CVE-2024-3094)
**Source**: Veritasium (Derek Muller & Henry van Dyck) - "The Internet Was Weeks Away From Disaster And No One Knew" (53 min documentary)
**URL**: https://youtu.be/aoag03mSuXQ
**Analyzed & Ingested**: 2026-10-11T12:19:33.022532

---

## 1. Executive Summary
In March 2024, the global technology infrastructure narrowly escaped one of the most sophisticated, devastating cyber supply-chain attacks in computing history. An undercover actor using the persona "Jia Tan" spent over two years socially engineering their way into co-maintaining **XZ Utils** (the ubiquitous LZMA data compression package). They planted an intricately obfuscated backdoor into `liblzma` versions 5.6.0 and 5.6.1 designed to intercept OpenSSH (`sshd`) authentication routines and grant remote, unauthenticated, cryptographic root command execution.

The attack was caught mere weeks before spreading to production Linux distributions across billions of servers worldwide—not by automated security scanners, but by a single Microsoft engineer (**Andres Freund**) investigating microsecond CPU anomalies and Valgrind memory warnings during PostgreSQL benchmark testing.

---

## 2. Technical Anatomy of the Attack

### 2.1 The Dependency Chain & Attack Vector
- **OpenSSH (`sshd`)** does not directly link to `liblzma`.
- However, major Linux distributions (Debian, Ubuntu, Red Hat, Fedora) patched OpenSSH to support **`systemd-notify`** (allowing systemd to monitor sshd service readiness).
- `libsystemd` links to `liblzma` to support decompressing journal and log files.
- Consequently, whenever `sshd` booted on systemd-based Linux systems, `liblzma.so` was loaded directly into the root-privileged address space of `sshd`.

### 2.2 Infiltration & Social Engineering (2021–2024)
- **Lasse Collin**, the solo Finnish maintainer of XZ Utils, was exhausted, unpaid, and suffering from mental burnout.
- Starting in 2021, sockpuppet accounts ("Jigar Kumar", "Dennis Ens") bombarded Collin on the public mailing list with aggressive complaints about slow release cadences, pressuring him to bring on another co-maintainer.
- "Jia Tan" (`JiaT75`) presented as an exceptionally helpful, polite, and technically competent contributor, submitting bug fixes and clean commits over a span of two years to build absolute trust.
- In 2023, Collin granted Jia Tan commit rights and full release management authority.

### 2.3 Obfuscation & Delivery Mechanism
1. **The Hidden Binary Payload**: Jia Tan committed test binary files (`bad-3-corrupt_lzma2.xz` and `good-large_compressed.lzma`) disguised as test cases for corrupt compression streams. In reality, these files contained raw 64-bit x86-64 machine code fragments.
2. **Build-Time Extraction (Tarball vs Git)**: Jia Tan modified the `m4/build-to-host.m4` macro included only in the official release tarballs (not in the public GitHub git repository). During `./configure` and `make` on x86-64 Linux systems producing Debian/RPM packages:
   - Bash/sed commands stitched together the binary fragments from the test files.
   - A modified object file was compiled directly into `liblzma_la-crc64_fast.o`.
3. **Execution via GNU IFUNC (Indirect Functions)**:
   - When `liblzma` is loaded by the dynamic linker (`ld.so`), GNU IFUNC resolves architecture-optimized functions (like CRC64) before `main()` executes or privileges drop.
   - The backdoor hijacked this IFUNC hook to manipulate the Global Offset Table (GOT).
   - It redirected OpenSSH's `RSA_public_decrypt` pointer to the backdoor's handler (`_get_cpuid`).

### 2.4 Cryptographic Backdoor Architecture
- Traditional backdoors use hardcoded passwords or open reverse shells, which IDS/honeypots quickly detect.
- Jia Tan's backdoor hooked `RSA_public_decrypt`:
  - When an incoming SSH client presents an authentication certificate, the hooked function inspects the signature data.
  - The payload was signed using **Ed448 asymmetric cryptography**. The attacker embedded their public key inside the backdoor.
  - If (and only if) the incoming signature validates against the attacker's Ed448 public key, the backdoor decrypts the encapsulated payload and passes it directly to `system()` to run as root.
  - For all other connection attempts, the function passes control transparently back to normal OpenSSH RSA decryption.
  - **Zero observable footprint**: Third-party observers without the private key cannot trigger, authenticate, or inspect the backdoor.

---

## 3. How It Was Caught
- **Andres Freund** was profiling PostgreSQL database performance on Debian Sid (unstable).
- He noticed `ssh` logins were consuming unexpected CPU time and taking ~500ms longer than normal.
- Running Valgrind produced unusual memory errors pointing to `liblzma.so`.
- Inspecting `liblzma` revealed hidden symbol modifications, leading to immediate public disclosure on oss-security on March 29, 2024 (Good Friday).

---

## 4. Attribution & Profile ("Jia Tan")
- **Commit Timestamps**: Analyzed by researchers; followed an 09:00 to 17:00 UTC+2 or UTC+3 schedule (consistent with Eastern Europe / Russia). Observed no commits on Chinese holidays, but observed breaks aligning with Eastern European calendars.
- **Sophistication**: The multi-year patient timeline, operational security, cryptographic design (Ed448), and understanding of Linux toolchains point directly to state-sponsored advanced persistent threat (APT) groups.

---

## 5. Defensive Takeaways for the JOSIE Swarm
1. **Minimal Surface Area**: Never link heavyweight decompression or logging libraries into security-critical daemons (OpenSSH has since removed systemd-notify linkage).
2. **Deterministic & Audited Builds**: Verify reproducible builds from pristine git source rather than accepting opaque pre-packaged release tarballs.
3. **Anomalous Latency Profiling**: Treat unexplained 100ms+ timing regressions or CPU spikes as potential indicators of compromise (IOCs).
