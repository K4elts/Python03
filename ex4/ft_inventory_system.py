import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = {}
    try:
        for args in sys.argv[1:]:
            key, value = args.split(":")
            inventory[key] = int(value)
        print(inventory)
    except BaseException as e:
        print(e)
