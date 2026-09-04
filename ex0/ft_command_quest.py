import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        for arg in range(1, len(sys.argv)):
            print(f"Argument {arg}: {sys.argv[arg]}")
    print(f"Total arguments: {len(sys.argv)}")
