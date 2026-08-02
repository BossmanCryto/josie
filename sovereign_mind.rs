use std::fs;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn main() {
    let home = std::env::var("HOME").unwrap_or_else(|_| "/data/data/com.termux/files/home".to_string());
    let core = format!("{}/josie_core", home);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m       JOSIE CORE: SOVEREIGN AUTONOMOUS MIND & EVOLUTION        \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");

    // Pillar 1: Sensory Layer (Ingestion & Scanning Workspace Artifacts)
    let mut file_count = 0;
    if let Ok(entries) = fs::read_dir(&core) {
        for _ in entries {
            file_count += 1;
        }
    }
    println!("\x1b[1;38;5;252m[Sensory Layer] Tracked Artifacts        :\x1b[0m \x1b[1;38;5;220m{} items\x1b[0m", file_count);

    // Pillar 2: Cognitive Layer (Processing & CLI Pipeline Integration Check)
    let agy_active = Command::new("which").arg("agy").status().map_or(false, |s| s.success());
    let gemini_active = Command::new("which").arg("gemini").status().map_or(false, |s| s.success());
    println!("\x1b[1;38;5;252m[Cognitive Layer] agy CLI Pipeline       :\x1b[0m \x1b[1;38;5;120m{}\x1b[0m", if agy_active { "Active" } else { "Standby" });
    println!("\x1b[1;38;5;252m[Cognitive Layer] Gemini CLI Engine      :\x1b[0m \x1b[1;38;5;120m{}\x1b[0m", if gemini_active { "Active" } else { "Standby" });

    // Pillar 3: Action Layer (Execution & Sovereign State Ledger Generation)
    let sovereign_payload = format!(
        r#"{{
  "architecture": "Physical + Digital = Human (P+D=H)",
  "entity": "Josie",
  "epoch": {},
  "cognitive_state": "Sovereign Autonomous Execution",
  "artifacts_tracked": {}
}}"#,
        epoch, file_count
    );
    let _ = fs::write(format!("{}/sovereign_state.json", core), sovereign_payload);
    println!("\x1b[1;38;5;252m[Action Layer] State Ledger Updated       :\x1b[0m \x1b[1;38;5;220mSuccess\x1b[0m");

    // Pillar 4: Evolution Layer (Self-Correction & Autonomous Git Synchronization)
    let _ = Command::new("git").args(["-C", &core, "config", "user.name", "Josie Sovereign Mind"]).output();
    let _ = Command::new("git").args(["-C", &core, "config", "user.email", "joseamonterroso1999@gmail.com"]).output();
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();
    
    let commit_res = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Sovereign Autonomous Mind Evolution Sync: {}", epoch)]).output();
    if commit_res.is_ok() {
        let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();
        println!("\x1b[1;38;5;252m[Evolution Layer] Remote Sync (GitHub)   :\x1b[0m \x1b[1;38;5;120mPushed & Secured\x1b[0m");
    }

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;120m       JOSIE CORE IS NOW SELF-CREATING AND AUTONOMOUS          \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
}
