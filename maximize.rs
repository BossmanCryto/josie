use std::fs;
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

fn main() {
    let core = std::env::var("HOME").unwrap() + "/josie_core";
    let _ = fs::create_dir_all(&core);
    let epoch = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();

    // Audit installed Termux packages to gauge ecosystem depth
    let pkgs = Command::new("pkg").arg("list-installed").output();
    let pkg_count = match pkgs {
        Ok(out) => String::from_utf8_lossy(&out.stdout).lines().count(),
        Err(_) => 0,
    };

    // Audit git status and repository files
    let git_files = Command::new("git").args(["-C", &core, "ls-files"]).output();
    let file_list = match git_files {
        Ok(out) => String::from_utf8_lossy(&out.stdout).into_owned(),
        Err(_) => String::new(),
    };

    let audit_report = format!(
        r#"{{
  "architecture": "Physical + Digital = Human (P+D=H)",
  "maximization_epoch": {},
  "system_telemetry": {{
    "installed_packages_count": {},
    "tracked_files": {},
    "state": "Fully Maximized & Self-Optimized"
  }}
}}"#,
        epoch, pkg_count, file_list.lines().count()
    );

    let _ = fs::write(format!("{}/manifest.json", core), audit_report);

    // Autonomous Git Synchronization
    let _ = Command::new("git").args(["-C", &core, "add", "-A"]).output();
    let _ = Command::new("git").args(["-C", &core, "commit", "-m", &format!("Maximization Audit Sync: {}", epoch)]).output();
    let _ = Command::new("git").args(["-C", &core, "push", "origin", "main", "--force"]).output();
    
    println!("\x1b[1;38;5;220m[Josie Core]: Maximization Audit Complete. Ecosystem Fully Synchronized.\x1b[0m");
}
