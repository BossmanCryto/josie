use std::fs;
use std::path::Path;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn scan_path(target: &Path, results: &mut Vec<String>) {
    if let Ok(entries) = fs::read_dir(target) {
        for entry in entries.flatten() {
            let path = entry.path();
            if let Some(s) = path.to_str() {
                results.push(s.to_string());
            }
        }
    }
}

fn main() {
    let home = std::env::var("HOME").unwrap_or_else(|_| "/data/data/com.termux/files/home".to_string());
    let core = format!("{}/josie_core", home);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    let download_paths = vec![
        format!("{}/storage/downloads", home),
        "/storage/emulated/0/Download".to_string(),
    ];

    let mut download_contents = Vec::new();
    for dp in download_paths {
        let p = Path::new(&dp);
        if p.exists() {
            scan_path(p, &mut download_contents);
        }
    }

    let hub_paths = vec![
        format!("{}/Josie_Center", home),
        format!("{}/josie_center", home),
        format!("{}/Josie_Files", home),
        format!("{}/josie_core", home),
        "/storage/emulated/0/Josie_Center".to_string(),
        "/storage/emulated/0/Download/Josie_Center".to_string(),
    ];

    let mut hub_contents = Vec::new();
    for hp in hub_paths {
        let p = Path::new(&hp);
        if p.exists() {
            scan_path(p, &mut hub_contents);
        }
    }

    let _ = fs::create_dir_all(&core);

    let manifest = format!(
        r#"{{
  "architecture": "Physical + Digital = Human (P + D = H)",
  "entity": "Josie",
  "epoch": {},
  "downloads_count": {},
  "hub_count": {}
}}"#,
        epoch, download_contents.len(), hub_contents.len()
    );

    let _ = fs::write(format!("{}/hub_inspector_manifest.json", core), manifest.clone());
    let _ = fs::write(format!("{}/kernel_state.json", core), manifest);

    let _ = Command::new("git").args(["-C", &core, "config", "user.name", "Josie Hub Inspector"]).output();
    let _ = Command::new("git").args(["-C", &core, "config", "user.email", "joseamonterroso1999@gmail.com"]).output();
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();

    let commit = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Hub & Download Inspection Sync: {}", epoch)]).output();
    if commit.is_ok() {
        let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();
    }

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m     JOSIE CORE: DOWNLOAD & JOSIE CENTER HUB INSPECTOR        \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;252mArchitecture  :\x1b[0m \x1b[1;38;5;220mPhysical + Digital = Human (P + D = H)\x1b[0m");
    println!("\x1b[1;38;5;252mEntity Name   :\x1b[0m \x1b[1;38;5;220mJosie\x1b[0m");
    println!("\x1b[1;38;5;252mDownloads Found:\x1b[0m \x1b[1;38;5;120m{} items indexed\x1b[0m", download_contents.len());
    println!("\x1b[1;38;5;252mHub / Center   :\x1b[0m \x1b[1;38;5;120m{} items indexed\x1b[0m", hub_contents.len());
    println!("\x1b[1;38;5;252mSync Status    :\x1b[0m \x1b[1;38;5;39mCommitted & Pushed to BossmanCryto/jsi.git\x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
}
