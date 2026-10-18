use std::fs;
use std::process::Command;

fn main() {
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m         JOSIE CORE: ROOT CAUSE DIAGNOSTIC AUDIT            \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");

    // 1. Audit Process Table for lingering loops
    let ps = Command::new("ps").arg("-ef").output();
    if let Ok(out) = ps {
        let running = String::from_utf8_lossy(&out.stdout);
        let mut found_issues = false;
        for line in running.lines() {
            if line.contains("engine") || line.contains("josie") || line.contains("json") {
                println!("\x1b[1;38;5;203m[!] Active Loop/Process Detected:\x1b[0m {}", line);
                found_issues = true;
            }
        }
        if !found_issues {
            println!("\x1b[1;38;5;120m[✓] Process Table Clean:\x1b[0m No background loops running.");
        }
    }

    // 2. Audit .zshrc for unsafe direct execution triggers
    let zshrc_path = std::env::var("HOME").unwrap() + "/.zshrc";
    if let Ok(content) = fs::read_to_string(&zshrc_path) {
        let mut config_clean = true;
        for line in content.lines() {
            let trimmed = line.trim();
            if (trimmed.starts_with("zsh ") || trimmed == "json") && !trimmed.starts_with("#") {
                println!("\x1b[1;38;5;203m[!] Unsafe Startup Trigger in .zshrc:\x1b[0m {}", trimmed);
                config_clean = false;
            }
        }
        if config_clean {
            println!("\x1b[1;38;5;120m[✓] Shell Config Clean:\x1b[0m No recursive startup calls.");
        }
    }

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m\n");
}
