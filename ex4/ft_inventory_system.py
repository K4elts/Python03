import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = {}
    for args in sys.argv[1:]:
        if ":" not in args:
            print(f"Error - invalid parameter '{args}'")
            continue
        key, quantity = args.split(":", 1)
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            int_value = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
            continue
        inventory[key] = int_value
    print(f"Got inventory: {inventory}")
    key_list = list(inventory.keys())
    print(f"Item list: {key_list}")
    item_quantity = sum(inventory.values())
    print(f"Total quantity of the number items: {item_quantity}")
    if inventory:
        most_abundant = ""
        least_abundant = ""
        for key, value in inventory.items():
            percentage = (value / item_quantity) * 100
            print(f"Item {key} represents {round(percentage, 2)}%")
            if most_abundant == "" or value > inventory[most_abundant]:
                most_abundant = key
            if least_abundant == "" or value < inventory[least_abundant]:
                least_abundant = key
        print(f"Item most abundant: {most_abundant}",
              f"with quantity {inventory[most_abundant]}")
        print(f"Item least abundant: {least_abundant}",
              f"with quantity {inventory[least_abundant]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
