FILENAME = "wimbledon.csv"

def main():
    records = read_wimbledon_data(FILENAME)

    champion_to_count, countries = process_records(records)

    display_results(champion_to_count, countries)

def read_wimbledon_data(filename):

    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:

        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                # e.g. 1968,Rod Laver,AUS
                year = parts[0]
                champion = parts[1]
                country = parts[2]
                records.append([year, champion, country])
    return records

def process_records(records):
    champion_to_count = {}
    countries = set()

    for record in records:
        _, champion, country = record

        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1

        countries.add(country)

    return champion_to_count, countries

def display_results(champion_to_count, countries):
    print("Wimbledon Champions:")
    for champion, wins in champion_to_count.items():
        print(f"{champion} {wins}")

    print()
    sorted_countries = sorted(countries)
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))

if __name__ == "__main__":
    main()