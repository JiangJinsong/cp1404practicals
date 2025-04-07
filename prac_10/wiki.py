import wikipedia


def get_wikipedia_page():
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break

        try:
            # Try to get the page without autosuggestion.
            page = wikipedia.page(title, auto_suggest=False)
            print("\n" + page.title)
            # Print a brief summary (first 2 sentences)
            print(wikipedia.summary(title, sentences=2))
            print(page.url + "\n")
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options, "\n")
        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!\n')


if __name__ == "__main__":
    get_wikipedia_page()