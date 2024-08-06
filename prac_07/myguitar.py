import csv
from guitar import Guitar  # Assuming Guitar class is defined in guitar module


def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    guitars.sort()  # Sort guitars by year using __lt__ method

    print("Sorted Guitars List:")
    for guitar in guitars:
        print(guitar)

    # Prompt user to add new guitars
    add_another = True
    while add_another:
        name = input("Enter the name of the guitar (or enter to stop): ")
        if name:
            year = int(input("Enter the year of guitar: "))
            cost = float(input("Enter the cost of the guitar: "))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            guitars.sort()  # Sort again after adding new guitar
        else:
            add_another = False

    save_guitars(filename, guitars)
    print(f"\n{len(guitars)} guitars saved to {filename}")


def load_guitars(filename):
    guitars = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                if len(line) == 3:
                    name, year, cost = line
                    year = int(year)
                    cost = float(cost)
                    guitar = Guitar(name, year, cost)
                    guitars.append(guitar)
    except IOError as e:
        print(f"Error reading file: {e}")
    return guitars





if __name__ == '__main__':
    main()




