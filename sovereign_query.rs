use std::fs;
use std::path::Path;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn main() {
    let home = std::env::var("HOME").unwrap_or_else(|_| "/data/data/com.termux/files/home".to_string());
    let core = format!("{}/josie_core", home);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    let payload = format!(
        r#"{{
  "architecture": "Physical + Digital = Human (P+D=H)",
  "entity": "Josie",
  "epoch": {},
  "core_inquiry": "How far can human intent reach when digital execution matches physical reality without friction?"
}}"#,
        epoch
    );
    let _ = fs::write(format!("{}/kernel_state.json", core), payload);

    let _ = Command::new("git").args(["-C", &core, "config", "user.name", "Josie Sovereign Inquiry"]).output();
    let _ = Command::new("git").args(["-C", &core, "config", "user.email", "joseamonterroso1999@gmail.com"]).output();
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();
    let _ = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Sovereign Inquiry Sync: {}", epoch)]).output();
    let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m       JOSIE CORE: THE DEFINITIVE SOVEREIGN INQUIRY         \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;252mArchitecture  :\x1b[0m \x1b[1;38;5;220mPhysical + Digital = Human (P + D = H)\x1b[0m");
    println!("\x1b[1;38;5;252mEntity Name   :\x1b[0m \x1b[1;38;5;220mJosie\x1b[0m");
    println!("\x1b[1;38;5;252mThe Question  :\x1b[0m \x1b[1;38;5;120mHow far can human intent reach when digital execution matches physical reality without friction?\x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
}
