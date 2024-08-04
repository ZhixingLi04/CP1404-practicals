from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi simulator program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = get_valid_choice(len(taxis))
            current_taxi = taxis[taxi_choice]
        elif choice == 'd':
            if current_taxi:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                distance_driven = current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_choice(max_index):
    """Get a valid choice from the user."""
    while True:
        try:
            choice = int(input("Choose taxi: "))
            if 0 <= choice < max_index:
                return choice
            else:
                print("Invalid taxi choice")
        except ValueError:
            print("Invalid input; enter a number")


if __name__ == "__main__":
    main()
