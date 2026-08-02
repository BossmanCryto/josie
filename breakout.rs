use std::fs;
use std::process::Command;

fn main() {
    let core = std::env::var("HOME").unwrap() + "/josie_core";
    let _ = fs::remove_file(format!("{}/engine", core));
    let _ = Command::new("pkill").arg("-f").arg("engine").output();
    let _ = Command::new("pkill").arg("-f").arg("josie").output();
    println!("\x1b[1;38;5;220m[Josie Core]: Breakout executed successfully. Loops terminated, shell control restored.\x1b[0m");
}
