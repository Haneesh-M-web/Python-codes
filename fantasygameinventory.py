def display_inventory(inventory):
    """Display the player's inventory in a formatted way"""
    print("Inventory:")
    total_items = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count
    print(f"Total number of items: {total_items}\n")

def add_to_inventory(inventory, added_items):
    """Add loot to the inventory"""
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

def print_table(inventory, order=None):
    """Print the inventory as a well-organized table"""
    print("Inventory:")
    print("{:>10} | {:<10}".format("count", "item name"))
    print("-" * 23)
    
    if order == "count,asc":
        items = sorted(inventory.items(), key=lambda x: x[1])
    elif order == "count,desc":
        items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    else:
        items = inventory.items()
    
    for item, count in items:
        print("{:>10} | {:<10}".format(count, item))
    
    total = sum(inventory.values())
    print("-" * 23)
    print(f"Total items: {total}\n")

def import_inventory(filename="import_inventory.csv"):
    """Import inventory from CSV file"""
    import csv
    inventory = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    inventory[row[0]] = int(row[1])
        print(f"Inventory imported from {filename}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error importing file: {e}")
    return inventory

def export_inventory(inventory, filename="export_inventory.csv"):
    """Export inventory to CSV file"""
    import csv
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for item, count in inventory.items():
                writer.writerow([item, count])
        print(f"Inventory exported to {filename}")
    except Exception as e:
        print(f"Error exporting file: {e}")

def main():
    # Starting inventory
    inventory = {
        'rope': 1,
        'torch': 6,
        'gold coin': 42,
        'dagger': 1,
        'arrow': 12
    }
    
    while True:
        print("\nFantasy Game Inventory System")
        print("1. Display inventory")
        print("2. Add loot to inventory")
        print("3. Display sorted inventory table")
        print("4. Import inventory from file")
        print("5. Export inventory to file")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            loot = input("Enter loot items separated by commas: ").split(',')
            loot = [item.strip() for item in loot if item.strip()]
            inventory = add_to_inventory(inventory, loot)
            print("Loot added to inventory!")
        elif choice == '3':
            print("\nSort options:")
            print("1. No sorting")
            print("2. Sort by count (ascending)")
            print("3. Sort by count (descending)")
            sort_choice = input("Enter sort option (1-3): ")
            if sort_choice == '1':
                print_table(inventory)
            elif sort_choice == '2':
                print_table(inventory, "count,asc")
            elif sort_choice == '3':
                print_table(inventory, "count,desc")
            else:
                print("Invalid choice, displaying unsorted")
                print_table(inventory)
        elif choice == '4':
            filename = input("Enter filename (default: import_inventory.csv): ") or "import_inventory.csv"
            imported = import_inventory(filename)
            if imported:
                inventory = imported
        elif choice == '5':
            filename = input("Enter filename (default: export_inventory.csv): ") or "export_inventory.csv"
            export_inventory(inventory, filename)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()