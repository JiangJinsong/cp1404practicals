COLOR_TO_CODE = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aquamarine": "#7fffd4",
    "beige": "#f5f5dc",
    "coral": "#ff7f50",
    "cyan": "#00ffff",
    "darkgreen": "#006400",
    "gold": "#ffd700",
    "hotpink": "#ff69b4",
    "lavender": "#e6e6fa"
}

color_name = input("Enter a color name: ").strip().lower()
while color_name != "":
    try:
        print(f"{color_name.title()} has the hex code {COLOR_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid colour name")
    color_name = input("Enter a color name: ").strip().lower()

print("Goodbye!")