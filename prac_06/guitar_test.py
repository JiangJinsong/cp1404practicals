from guitar import Guitar

def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    expected_age = 100
    expected_vintage = True

    guitar1 = Guitar(name, year, cost)
    actual_age = guitar1.get_age()
    actual_vintage = guitar1.is_vintage()

    print(f"{guitar1.name} get_age() - Expected {expected_age}. Got {actual_age}")
    print(f"{guitar1.name} is_vintage() - Expected {expected_vintage}. Got {actual_vintage}")
    print()

    name2 = "Another Guitar"
    year2 = 2013
    cost2 = 1000.0
    expected_age2 = 9
    expected_vintage2 = False

    guitar2 = Guitar(name2, year2, cost2)
    actual_age2 = guitar2.get_age()
    actual_vintage2 = guitar2.is_vintage()

    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {actual_age2}")
    print(f"{guitar2.name} is_vintage() - Expected {expected_vintage2}. Got {actual_vintage2}")

if __name__ == "__main__":
    main()
