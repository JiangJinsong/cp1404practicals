"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    data = []
    with open(FILENAME, "r") as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data

def display_subject_details(data):
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

main()
