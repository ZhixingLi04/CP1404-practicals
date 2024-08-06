from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    # Comment out for actual user input
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Uncomment for actual user input
    adding_guitars = True
    while adding_guitars:
        name = input("Name: ").strip()
        if name == "":
            adding_guitars = False
        else:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost:,.2f} added.")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:20,.2f}{vintage_string}")



if __name__ == "__main__":
    main()


