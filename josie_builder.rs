use std::fs;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn main() {
    let core_root = std::env::var("HOME").unwrap() + "/josie_core";
    let ledger_path = format!("{}/kernel_state.json", core_root);
    
    let _ = fs::create_dir_all(&core_root);
    
    let timestamp = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_secs();

    let ledger_data = format!(
        r#"{{
  "architecture": "Physical + Digital = Human (P+D=H)",
  "timestamp_epoch": {},
  "engine": "Universal Rust-Zsh Automated CLI",
  "status": "Fully Autonomous and Functional"
}}"#,
        timestamp
    );
    
    let _ = fs::write(&ledger_path, ledger_data);
    
    // Autonomous Git Sync Engine
    let _ = Command::new("git").args(["-C", &core_root, "add", "-A"]).output();
    let _ = Command::new("git").args(["-C", &core_root, "commit", "-m", &format!("Autonomous CLI Rebuild Sync: {}", timestamp)]).output();
    let _ = Command::new("git").args(["-C", &core_root, "push", "origin", "main", "--force"]).output();
}
