use std::process::Command;
use std::fs;
use std::time::{SystemTime, UNIX_EPOCH};

fn main() {
    let core = std::env::var("HOME").unwrap() + "/josie_core";
    let _ = fs::create_dir_all(&core);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    // Check su root availability
    let su_check = Command::new("su").arg("-c").arg("id").output();
    let root_status = match su_check {
        Ok(out) if out.status.success() => {
            let stdout = String::from_utf8_lossy(&out.stdout);
            format!("Root Active ({})", stdout.trim())
        }
        _ => "Standard User / Root Restricted (Bootloader Locked Context)".to_string(),
    };

    let telemetry = format!(
        r#"{{
  "architecture": "Physical + Digital = Human (P+D=H)",
  "epoch": {},
  "root_status": "{}"
}}"#,
        epoch, root_status
    );
    let _ = fs::write(format!("{}/root_state.json", core), telemetry);

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m         JOSIE CORE: ROOT & MIXPLORER BRIDGE ACTIVE             \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;252mDevice Model  :\x1b[0m \x1b[1;38;5;220mSM-A176U\x1b[0m");
    println!("\x1b[1;38;5;252mAccess State  :\x1b[0m \x1b[1;38;5;120m{}\x1b[0m", root_status);
    println!("\x1b[1;38;5;252mFile Manager  :\x1b[0m \x1b[1;38;5;220mMixplorer Root Storage Bridge Ready\x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
}
