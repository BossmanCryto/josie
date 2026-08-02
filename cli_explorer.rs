use std::fs;
use std::path::Path;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn visit_dirs(dir: &Path, cb: &mut dyn FnMut(&Path)) -> std::io::Result<()> {
    if dir.is_dir() {
        for entry in fs::read_dir(dir)? {
            let entry = entry?;
            let path = entry.path();
            if path.is_dir() {
                // Skip hidden git directories to keep output clean
                if !path.file_name().map_or(false, |n| n == ".git") {
                    visit_dirs(&path, cb)?;
                }
            } else {
                cb(&path);
            }
        }
    }
    Ok(())
}

fn main() {
    let core = std::env::var("HOME").unwrap() + "/josie_core";
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;220m      JOSIE CORE: COMPREHENSIVE CLI WORKSPACE INSPECTOR         \x1b[0m");
    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
    println!("\x1b[1;38;5;252mArchitecture  :\x1b[0m \x1b[1;38;5;220mPhysical + Digital = Human (P + D = H)\x1b[0m");
    println!("\x1b[1;38;5;252mWorkspace Path:\x1b[0m \x1b[1;38;5;39m{}\x1b[0m", core);
    println!("\x1b[1;38;5;252mTimestamp     :\x1b[0m \x1b[1;38;5;220m{}\x1b[0m", epoch);
    println!("\x1b[1;38;5;39m────────────────────────────────────────────────────────────────\x1b[0m");

    println!("\x1b[1;38;5;120m[Scanning Workspace Files & Code Assets]:\x1b[0m");
    
    let mut file_count = 0;
    let _ = visit_dirs(Path::new(&core), &mut |path| {
        file_count += 1;
        let relative = path.strip_prefix(&core).unwrap_or(path);
        if let Ok(metadata) = fs::metadata(path) {
            let size = metadata.len();
            println!("  • {:?} ({membership} bytes)", relative, membership = size);
        }
    });

    println!("\x1b[1;38;5;39m────────────────────────────────────────────────────────────────\x1b[0m");
    println!("\x1b[1;38;5;252mTotal Tracked Artifacts :\x1b[0m \x1b[1;38;5;220m{}\x1b[0m", file_count);

    // Git Sync
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();
    let _ = Command::new("git").args(["-C", &core, "commit", "-m", &format!("CLI Comprehensive Scan Sync: {}", epoch)]).output();
    let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();

    println!("\x1b[1;38;5;39m════════════════════════════════════════════════════════════════\x1b[0m");
}
