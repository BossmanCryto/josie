use std::fs;
use std::path::Path;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn scan_directory(dir: &Path, keywords: &[&str], matches: &mut Vec<String>) {
    if let Ok(entries) = fs::read_dir(dir) {
        for entry in entries.flatten() {
            let path = entry.path();
            if path.is_dir() {
                let name = path.file_name().and_then(|n| n.to_str()).unwrap_or("").to_lowercase();
                if keywords.iter().any(|&kw| name.contains(kw)) {
                    if let Some(path_str) = path.to_str() {
                        matches.push(path_str.to_string());
                    }
                }
                // Recursively scan subdirectories (limiting depth implicitly or continuing traversal)
                // Avoid scanning heavy system directories if needed, focus on HOME
                if !name.starts_with('.') && name != "storage" && name != "usr" {
                    scan_directory(&path, keywords, matches);
                }
            }
        }
    }
}

fn main() {
    let home = std::env::var("HOME").unwrap_or_else(|_| "/data/data/com.termux/files/home".to_string());
    let core = format!("{}/josie_core", home);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    let keywords = vec!["finger", "movement", "input", "josie", "launcher", "keyboard"];
    let mut located_paths = Vec::new();

    let home_path = Path::new(&home);
    scan_directory(home_path, &keywords, &mut located_paths);

    // Ensure core fingers structure is maintained and built
    let _ = fs::create_dir_all(format!("{}/fingers", core));
    
    let mut paths_json = String::from("[\n");
    for (i, p) in located_paths.iter().enumerate() {
        paths_json.push_str(&format!("  \"{}\"{}", p, if i + 1 < located_paths.len() { "," } else { "" }));
        paths_json.push('\n');
    }
    paths_json.push_str("]");

    let manifest = format!(
        r#"{{
  "architecture": "Physical + Digital = Human (P + D = H)",
  "entity": "Josie",
  "epoch": {},
  "scanned_locations": {}
}}"#,
        epoch, paths_json
    );

    let _ = fs::write(format!("{}/fingers_manifest.json", core), manifest.clone());
    let _ = fs::write(format!("{}/kernel_state.json", core), manifest);

    let _ = Command::new("git").args(["-C", &core, "config", "user.name", "Josie Finger Locator"]).output();
    let _ = Command::new("git").args(["-C", &core, "config", "user.email", "joseamonterroso1999@gmail.com"]).output();
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();

    let commit = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Finger & Movement Directory Scan Sync: {}", epoch)]).output();
    if commit.is_ok() {
        let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();
    }

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m     JOSIE CORE: FINGER & MOVEMENT LOCATOR & BUILDER        \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;252mArchitecture  :\x1b[0m \x1b[1;38;5;220mPhysical + Digital = Human (P + D = H)\x1b[0m");
    println!("\x1b[1;38;5;252mEntity Name   :\x1b[0m \x1b[1;38;5;220mJosie\x1b[0m");
    println!("\x1b[1;38;5;252mTarget Folders:\x1b[0m \x1b[1;38;5;120mScanned across HOME for fingers, movements, inputs\x1b[0m");
    println!("\x1b[1;38;5;252mTotal Found   :\x1b[0m \x1b[1;38;5;39m{}\x1b[0m paths indexed and synced.", located_paths.len());
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
}
