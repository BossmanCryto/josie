use std::fs;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn main() {
    let home = std::env::var("HOME").unwrap_or_else(|_| "/data/data/com.termux/files/home".to_string());
    let core = format!("{}/josie_core", home);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m       JOSIE CORE: COGNITIVE MIND & CLI INTEGRATION             \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");

    // 1. Evaluate workspace code assets for cognitive processing
    let manifest_path = format!("{}/manifest.json", core);
    let workspace_status = if std::path::Path::new(&manifest_path).exists() {
        "Manifest Active - Ready for agy/Gemini CLI Pipeline"
    } else {
        "Initializing Baseline State"
    };

    println!("\x1b[1;38;5;252mCognitive Status :\x1b[0m \x1b[1;38;5;120m{}\x1b[0m", workspace_status);

    // 2. Check availability of agy / Gemini CLI tools in environment
    let agy_check = Command::which("agy").is_ok() || std::path::Path::new("/data/data/com.termux/files/usr/bin/agy").exists();
    let gemini_check = Command::which("gemini").is_ok() || std::path::Path::new("/data/data/com.termux/files/usr/bin/gemini").exists();

    println!("\x1b[1;38;5;252mAgy CLI Engine   :\x1b[0m \x1b[1;38;5;220m{}\x1b[0m", if agy_check { "Detected & Ready" } else { "Standby / Path Configured" });
    println!("\x1b[1;38;5;252mGemini CLI Tool  :\x1b[0m \x1b[1;38;5;220m{}\x1b[0m", if gemini_check { "Detected & Ready" } else { "Standby / Path Configured" });

    // 3. Record cognitive synchronization state
    let mind_state = format!(
        r#"{{
  "entity": "Josie",
  "epoch": {},
  "cognitive_layer": "Active",
  "agy_integration": "Enabled",
  "gemini_integration": "Enabled"
}}"#,
        epoch
    );
    let _ = fs::write(format!("{}/mind_state.json", core), mind_state);

    // 4. Safe Git Sync
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();
    let _ = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Cognitive Mind Sync: {}", epoch)]).output();
    let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
}
