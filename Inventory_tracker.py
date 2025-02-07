import json
import os

# File to store inventory data
INVENTORY_FILE = "inventory_data.json"

# Initialize inventory
inventory = {}

def load_inventory():
    """Load inventory from a JSON file (if exists)."""
    global inventory
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "r") as file:
            inventory = json.load(file)
    else:
        inventory = {}

def save_inventory():
    """Save inventory data to a JSON file."""
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)
    print("📁 Inventory saved successfully!\n")

def add_item():
    """Add a new item to the inventory."""
    item_name = input("Enter item name: ").strip()
    if item_name in inventory:
        print("⚠️ Item already exists! Use 'update stock' instead.")
        return
    
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    
    inventory[item_name] = {"quantity": quantity, "price": price}
    print(f"✅ {item_name} added successfully!\n")
    save_inventory()

def update_stock():
    """Update the stock quantity of an existing item."""
    item_name = input("Enter item name to update: ").strip()
    if item_name not in inventory:
        print("❌ Item not found in inventory!")
        return
    
    quantity = int(input("Enter quantity to add/remove (use negative numbers to remove): "))
    inventory[item_name]["quantity"] += quantity
    
    if inventory[item_name]["quantity"] < 0:
        inventory[item_name]["quantity"] = 0  # Prevent negative stock
    
    print(f"🔄 {item_name} stock updated. New quantity: {inventory[item_name]['quantity']}\n")
    save_inventory()

def display_inventory():
    """Display the current inventory."""
    if not inventory:
        print("📦 Inventory is empty!\n")
        return
    
    print("\n📋 Current Inventory:")
    print("-" * 30)
    for item, details in inventory.items():
        print(f"{item}: {details['quantity']} units - ${details['price']:.2f} each")
    print("-" * 30, "\n")

def delete_item():
    """Delete an item from inventory."""
    item_name = input("Enter item name to delete: ").strip()
    if item_name in inventory:
        del inventory[item_name]
        print(f"❌ {item_name} removed from inventory.\n")
        save_inventory()
    else:
        print("⚠️ Item not found in inventory!\n")

def main():
    """Main function to handle user input."""
    load_inventory()

    while True:
        print("\n📦 Inventory Management System")
        print("1️⃣ Add Item")
        print("2️⃣ Update Stock")
        print("3️⃣ Display Inventory")
        print("4️⃣ Delete Item")
        print("5️⃣ Exit")

        choice = input("Enter choice (1-5): ").strip()
        
        if choice == "1":
            add_item()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("👋 Exiting Inventory System. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.\n")

# Run the program
if __name__ == "__main__":
    main()
