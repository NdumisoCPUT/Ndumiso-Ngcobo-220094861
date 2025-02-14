use std::collections::HashMap;
use std::io;

struct Inventory {
    items: HashMap<String, u32>,
}

impl Inventory {
    fn new() -> Inventory {
        Inventory {
            items: HashMap::new(),
        }
    }

    fn add_item(&mut self, item: String, quantity: u32) {
        let count = self.items.entry(item).or_insert(0);
        *count += quantity;
        println!("✅ Item added successfully!");
    }

    fn display_inventory(&self) {
        println!("\n📦 Current Inventory:");
        for (item, quantity) in &self.items {
            println!("{}: {} units", item, quantity);
        }
    }
}

fn main() {
    let mut inventory = Inventory::new();

    loop {
        println!("\n📦 Inventory Management System");
        println!("1️⃣ Add Item");
        println!("2️⃣ Display Inventory");
        println!("3️⃣ Exit");
        
        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Failed to read input");
        
        match choice.trim() {
            "1" => {
                let mut item = String::new();
                println!("Enter item name: ");
                io::stdin().read_line(&mut item).expect("Failed to read input");

                let mut quantity = String::new();
                println!("Enter quantity: ");
                io::stdin().read_line(&mut quantity).expect("Failed to read input");

                let quantity: u32 = quantity.trim().parse().expect("Invalid number!");
                inventory.add_item(item.trim().to_string(), quantity);
            }
            "2" => inventory.display_inventory(),
            "3" => {
                println!("👋 Exiting... Goodbye!");
                break;
            }
            _ => println!("❌ Invalid choice! Try again."),
        }
    }
}
