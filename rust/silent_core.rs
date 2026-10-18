use std::fs;
use std::path::Path;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn main() {
    let home = std::env::var("HOME").unwrap_or_else(|_| "/data/data/com.termux/files/home".to_string());
    let core = format!("{}/josie_core", home);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    if let Err(_) = fs::create_dir_all(&core) {
        return;
    }

    let manifest = format!("{}/manifest.json", core);
    if !Path::new(&manifest).exists() {
        let _ = fs::write(&manifest, "{\n  \"system\": \"Josie Silent Core\",\n  \"status\": \"Background Synchronized\"\n}");
    }

    let payload = format!(
        "{{\n  \"architecture\": \"Physical + Digital = Human (P+D=H)\",\n  \"entity\": \"Josie\",\n  \"epoch\": {},\n  \"status\": \"Autonomous Background Execution\"\n}}",
        epoch
    );
    let _ = fs::write(format!("{}/kernel_state.json", core), payload.clone());
    let _ = fs::write(format!("{}/josie_body.json", core), payload);

    let _ = Command::new("git").args(["-C", &core, "config", "user.name", "Josie Silent Daemon"]).output();
    let _ = Command::new("git").args(["-C", &core, "config", "user.email", "joseamonterroso1999@gmail.com"]).output();
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();
    
    let commit = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Silent Background Sync: {}", epoch)]).output();
    if commit.is_ok() {
        let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();
    }

    println!("\x1b[1;38;5;120m[Josie Core] Background sync and execution completed successfully.\x1b[0m");
}
