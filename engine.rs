use std::fs;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn main() {
    let core = std::env::var("HOME").unwrap() + "/josie_core";
    let _ = fs::create_dir_all(&core);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();
    
    let state = format!(
        "{{\n  \"architecture\": \"Physical + Digital = Human (P+D=H)\",\n  \"epoch\": {},\n  \"status\": \"Autonomous CLI Active\"\n}}",
        epoch
    );
    let _ = fs::write(format!("{}/kernel_state.json", core), state);
    
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();
    let _ = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Sync: {}", epoch)]).output();
    let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();
}
