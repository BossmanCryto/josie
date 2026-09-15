#!/data/data/com.termux/files/usr/bin/env bash
# Base44 High-Efficiency & Zero-Loss Byte Encoding Engine
# QR-Compatible / Alphanumeric 44-Character Matrix: 0-9, A-Z, a-h

BASE44_ALPHABET="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh"

base44_encode() {
    local input="$1"
    python3 -c "
import sys
alphabet = '$BASE44_ALPHABET'
data = sys.argv[1].encode('utf-8') if len(sys.argv) > 1 else b''
if not data:
    print('')
    sys.exit(0)

# Count leading zero bytes for exact byte padding preservation
null_count = 0
for b in data:
    if b == 0:
        null_count += 1
    else:
        break

num = int.from_bytes(data, 'big')
if num == 0:
    print(alphabet[0] * len(data))
    sys.exit(0)

res = []
while num > 0:
    num, rem = divmod(num, 44)
    res.append(alphabet[rem])

encoded = (alphabet[0] * null_count) + ''.join(reversed(res))
print(encoded)
" "$input"
}

base44_decode() {
    local encoded="$1"
    python3 -c "
import sys
alphabet = '$BASE44_ALPHABET'
encoded = sys.argv[1] if len(sys.argv) > 1 else ''
if not encoded:
    print('')
    sys.exit(0)

null_count = 0
for char in encoded:
    if char == alphabet[0]:
        null_count += 1
    else:
        break

num = 0
for char in encoded[null_count:]:
    num = num * 44 + alphabet.index(char)

if num == 0 and null_count > 0:
    print((b'\x00' * null_count).decode('utf-8', errors='ignore'))
    sys.exit(0)

byte_len = (num.bit_length() + 7) // 8
data = (b'\x00' * null_count) + num.to_bytes(byte_len, 'big')
print(data.decode('utf-8', errors='ignore'))
" "$encoded"
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    test_str="${1:-JosieBase44Matrix_AGI_Core}"
    enc=$(base44_encode "$test_str")
    dec=$(base44_decode "$enc")
    echo -e "════════════════════════════════════════════════════════════════"
    echo -e "       BASE44 ZERO-LOSS ENCODING ENGINE DEMONSTRATION           "
    echo -e "════════════════════════════════════════════════════════════════"
    echo -e "  Original Payload : $test_str"
    echo -e "  Base44 Encoded   : $enc"
    echo -e "  Base44 Decoded   : $dec"
    echo -e "════════════════════════════════════════════════════════════════"
fi
