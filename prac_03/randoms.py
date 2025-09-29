import random

def main():
    print(random.randint(5, 20))
    print(random.randrange(3, 10, 2))
    print(f"{random.uniform(2.5, 5.5):.2f}")

if __name__ == "__main__":
    main()