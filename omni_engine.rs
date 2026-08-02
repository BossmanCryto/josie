use std::fs;
use std::path::Path;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn main() {
    let home = std::env::var("HOME").unwrap_or_else(|_| "/data/data/com.termux/files/home".to_string());
    let core = format!("{}/josie_core", home);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    if let Err(_) = fs::create_dir_all(&core) {
        eprintln!("Error: Failed to create workspace.");
        return;
    }

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m       JOSIE OMNI-CORE: UNIVERSAL EXECUTION ENGINE              \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");

    let manifest = format!("{}/manifest.json", core);
    if !Path::new(&manifest).exists() {
        let default_data = "{\n  \"system\": \"Josie Omni-Core\",\n  \"status\": \"Universal & Optimized\"\n}";
        let _ = fs::write(&manifest, default_data);
    }

    let payload = format!(
        "{{\n  \"architecture\": \"Physical + Digital = Human (P+D=H)\",\n  \"entity\": \"Josie\",\n  \"epoch\": {},\n  \"status\": \"Universal Unified Execution\"\n}}",
        epoch
    );
    let _ = fs::write(format!("{}/kernel_state.json", core), payload.clone());
    let _ = fs::write(format!("{}/josie_body.json", core), payload);

    let _ = Command::new("git").args(["-C", &core, "config", "user.name", "Josie Omni Engine"]).output();
    let _ = Command::new("git").args(["-C", &core, "config", "user.email", "joseamonterroso1999@gmail.com"]).output();
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();
    
    let commit = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Omni-Core Universal Sync: {}", epoch)]).output();
    if commit.is_ok() {
        let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();
    }

    println!("\x1b[1;38;5;252mWorkspace Path  :\x1b[0m \x1b[1;38;5;39m{}\x1b[0m", core);
    println!("\x1b[1;38;5;252mSystem Status   :\x1b[0m \x1b[1;38;5;120mUniversal Engine Compiled & Synchronized\x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
}
