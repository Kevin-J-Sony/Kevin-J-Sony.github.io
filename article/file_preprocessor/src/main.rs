use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        eprintln!("Usage: cargo run <filename>");
        return;
    }

    let filename = &args[1];
    let contents = fs::read_to_string(filename);

    match contents {
        Ok(data) => {
            // Example preprocessing: uppercase
            let processed = data.to_uppercase();
            
            println!("Processed content:\n{}", processed);
        }
        Err(e) => {
            eprintln!("Error reading file: {}", e);
        }
    }

}
