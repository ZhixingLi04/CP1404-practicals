"""
Hexadecimal Colour Codes Lookup
Estimate: 30 minutes
"""



# Define a constant dictionary of colour names and their corresponding hex codes
COLOUR_CODES = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}


def main():
    while True:
        color_name = input("Enter a color name (or blank to quit): ").strip().upper()

        if color_name == "":
            break

        color_code = COLOUR_CODES.get(color_name, "Unknown")
        print(f"The hexadecimal code for {color_name} is {color_code}")


main()
