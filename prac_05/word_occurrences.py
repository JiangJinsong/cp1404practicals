def main():
    text = input("Text: ")
    words = text.split()

    # Count the occurrences of each word using a dictionary
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Determine the length of the longest word for alignment
    max_length = max(len(word) for word in word_counts)

    # Sort the words alphabetically
    sorted_words = sorted(word_counts.keys())

    # Print each word aligned to the max length, then print the count
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_counts[word]}")

# Run the program
main()