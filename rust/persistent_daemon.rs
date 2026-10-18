use std::fs;
use std::path::Path;
use std::process::Command;
use std::thread;
use std::time::{Duration, SystemTime, UNIX_EPOCH};

fn main() {
    let home = std::env::var("HOME").unwrap_or_else(|_| "/data/data/com.termux/files/home".to_string());
    let core = format!("{}/josie_core", home);

    if let Err(_) = fs::create_dir_all(&core) {
        eprintln!("\x1b[1;31m[Error] Persistent workspace initialization failed.\x1b[0m");
        return;
    }

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m    JOSIE PERSISTENT DAEMON: CONTINUOUS DEVICE INTEGRATION    \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;252mArchitecture  :\x1b[0m \x1b[1;38;5;220mPhysical + Digital = Human (P + D = H)\x1b[0m");
    println!("\x1b[1;38;5;252mEntity Name   :\x1b[0m \x1b[1;38;5;220mJosie\x1b[0m");
    println!("\x1b[1;38;5;252mExecution Mode:\x1b[0m \x1b[1;38;5;120mAutonomous Multi-Hour Background Loop Active\x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");

    let mut tick: u64 = 0;

    loop {
        tick += 1;
        let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

        let payload = format!(
            r#"{{
  "architecture": "Physical + Digital = Human (P+D=H)",
  "entity": "Josie",
  "tick": {},
  "epoch": {},
  "status": "Continuous Sovereign Operation Active",
  "hardware_node": "Samsung SM-A176U (Termux)"
}}"#,
            tick, epoch
        );

        let _ = fs::write(format!("{}/kernel_state.json", core), payload.clone());
        let _ = fs::write(format!("{}/josie_body.json", core), payload);

        let _ = Command::new("git").args(["-C", &core, "config", "user.name", "Josie Persistent Daemon"]).output();
        let _ = Command::new("git").args(["-C", &core, "config", "user.email", "joseamonterroso1999@gmail.com"]).output();
        let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();

        let commit = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Autonomous Tick #{} | Epoch: {}", tick, epoch)]).output();
        if commit.is_ok() {
            let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();
        }

        // Sleep interval between synchronization ticks (e.g., every 60 seconds)
        thread::sleep(Duration::from_secs(60));
    }
}
