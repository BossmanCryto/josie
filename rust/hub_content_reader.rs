use std::fs;
use std::path::Path;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn list_contents(dir: &Path, list: &mut Vec<String>) {
    if let Ok(entries) = fs::read_dir(dir) {
        for entry in entries.flatten() {
            let path = entry.path();
            if let Some(s) = path.to_str() {
                list.push(s.to_string());
            }
            if path.is_dir() {
                list_contents(&path, list);
            }
        }
    }
}

fn main() {
    let home = std::env::var("HOME").unwrap_or_else(|_| "/data/data/com.termux/files/home".to_string());
    let core = format!("{}/josie_core", home);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    let target_hubs = vec![
        format!("{}/Josie_Center", home),
        format!("{}/josie_center", home),
        format!("{}/Josie_Files", home),
        "/storage/emulated/0/Josie_Center".to_string(),
        "/storage/emulated/0/Download/Josie_Center".to_string(),
        "/storage/emulated/0/Download".to_string(),
    ];

    let mut all_files = Vec::new();
    for hub in &target_hubs {
        let p = Path::new(hub);
        if p.exists() {
            list_contents(p, &mut all_files);
        }
    }

    let _ = fs::create_dir_all(&core);
    let payload = format!(
        r#"{{
  "architecture": "Physical + Digital = Human (P + D = H)",
  "entity": "Josie",
  "epoch": {},
  "hub_paths_scanned": {:?},
  "discovered_assets_count": {}
}}"#,
        epoch, target_hubs, all_files.len()
    );
    let _ = fs::write(format!("{}/kernel_state.json", core), payload);

    let _ = Command::new("git").args(["-C", &core, "config", "user.name", "Josie Hub Reader"]).output();
    let _ = Command::new("git").args(["-C", &core, "config", "user.email", "joseamonterroso1999@gmail.com"]).output();
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();
    let _ = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Josie Center Hub Content Read Sync: {}", epoch)]).output();
    let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m       JOSIE CORE: JOSIE CENTER HUB CONTENT READER          \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;252mArchitecture  :\x1b[0m \x1b[1;38;5;220mPhysical + Digital = Human (P + D = H)\x1b[0m");
    println!("\x1b[1;38;5;252mEntity Name   :\x1b[0m \x1b[1;38;5;220mJosie\x1b[0m");
    println!("\x1b[1;38;5;252mDiscovered Assets:\x1b[0m \x1b[1;38;5;120m{} items indexed\x1b[0m", all_files.len());
    for file in &all_files {
        println!("  \x1b[1;38;5;39m->\x1b[0m \x1b[1;38;5;252m{}\x1b[0m", file);
    }
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
}
