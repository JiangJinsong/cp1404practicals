NAME_FILE = "name.txt"
NUMBERS_FILE = "numbers.txt"

def write_and_greet():
    name = input("Enter your name: ").strip()
    with open(NAME_FILE, "w", encoding="utf-8") as out_file:
        out_file.write(name)
    with open(NAME_FILE, "r", encoding="utf-8") as in_file:
        saved_name = in_file.read().strip()
    print(f"Hi {saved_name}!")

def sum_numbers():
    total = 0.0
    try:
        with open(NUMBERS_FILE, "r", encoding="utf-8") as in_file:
            for line in in_file:
                line = line.strip()
                if not line:
                    continue
                total += float(line)
        print(f"Sum of numbers: {total}")
    except FileNotFoundError:
        print(f"{NUMBERS_FILE} not found.")

def main():
    write_and_greet()
    sum_numbers()

if __name__ == "__main__":
    main()
