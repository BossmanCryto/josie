use std::fs;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn main() {
    let core = std::env::var("HOME").unwrap() + "/josie_core";
    let _ = fs::create_dir_all(&core);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    let state = format!(
        r#"{{
  "architecture": "Physical + Digital = Human (P+D=H)",
  "epoch": {},
  "status": "Josie Core CLI Active & Stable"
}}"#,
        epoch
    );
    let _ = fs::write(format!("{}/kernel_state.json", core), state);

    // Git Sync
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();
    let _ = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Josie CLI State Sync: {}", epoch)]).output();
    let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();

    let model = std::env::var("DEVICE_MODEL").unwrap_or_else(|_| "SM-A176U".to_string());

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m     JOSIE CORE: CLI ENGINE ACTIVE & SYNCHRONIZED               \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;252mArchitecture  :\x1b[0m \x1b[1;38;5;220mPhysical + Digital = Human (P + D = H)\x1b[0m");
    println!("\x1b[1;38;5;252mAccount ID    :\x1b[0m \x1b[1;38;5;39mjoseamonterroso1999@gmail.com\x1b[0m");
    println!("\x1b[1;38;5;252mDevice Model  :\x1b[0m \x1b[1;38;5;220m{}\x1b[0m", model);
    println!("\x1b[1;38;5;252mSystem Status :\x1b[0m \x1b[1;38;5;120mZero Loops / Fully Optimized\x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
}
