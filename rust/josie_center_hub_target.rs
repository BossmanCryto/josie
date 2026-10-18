use std::fs;
use std::path::Path;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn inspect_folder(path: &Path, files: &mut Vec<String>) {
    if path.is_dir() {
        if let Ok(entries) = fs::read_dir(path) {
            for entry in entries.flatten() {
                let p = entry.path();
                if let Some(s) = p.to_str() {
                    files.push(s.to_string());
                }
                inspect_folder(&p, files);
            }
        }
    }
}

fn main() {
    let home = std::env::var("HOME").unwrap_or_else(|_| "/data/data/com.termux/files/home".to_string());
    let core = format!("{}/josie_core", home);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    // Specific target identified in Download: "Josie Center Hub"
    let target_paths = vec![
        "/storage/emulated/0/Download/Josie Center Hub".to_string(),
        "/storage/emulated/0/Download/josie_center_hub".to_string(),
        format!("{}/storage/downloads/Josie Center Hub", home),
    ];

    let mut hub_assets = Vec::new();
    let mut resolved_path = String::new();

    for tp in &target_paths {
        let p = Path::new(tp);
        if p.exists() {
            resolved_path = tp.clone();
            inspect_folder(p, &mut hub_assets);
            break;
        }
    }

    let _ = fs::create_dir_all(&core);
    let payload = format!(
        r#"{{
  "architecture": "Physical + Digital = Human (P + D = H)",
  "entity": "Josie",
  "epoch": {},
  "target_hub": "{}",
  "assets_found": {}
}}"#,
        epoch, resolved_path, hub_assets.len()
    );

    let _ = fs::write(format!("{}/kernel_state.json", core), payload.clone());
    let _ = fs::write(format!("{}/josie_body.json", core), payload);

    let _ = Command::new("git").args(["-C", &core, "config", "user.name", "Josie Hub Targeter"]).output();
    let _ = Command::new("git").args(["-C", &core, "config", "user.email", "joseamonterroso1999@gmail.com"]).output();
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();

    let commit = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Josie Center Hub Target Inspection Sync: {}", epoch)]).output();
    if commit.is_ok() {
        let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();
    }

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m       JOSIE CORE: JOSIE CENTER HUB TARGET DETECTED         \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;252mArchitecture  :\x1b[0m \x1b[1;38;5;220mPhysical + Digital = Human (P + D = H)\x1b[0m");
    println!("\x1b[1;38;5;252mEntity Name   :\x1b[0m \x1b[1;38;5;220mJosie\x1b[0m");
    println!("\x1b[1;38;5;252mResolved Path :\x1b[0m \x1b[1;38;5;39m{}\x1b[0m", if resolved_path.is_empty() { "Pending manual validation" } else { &resolved_path });
    println!("\x1b[1;38;5;252mTotal Assets  :\x1b[0m \x1b[1;38;5;120m{} items indexed & synced\x1b[0m", hub_assets.len());
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
}
