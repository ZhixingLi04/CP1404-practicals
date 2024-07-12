"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "Car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
    # Create a new Car object with user-specified name and 100 units of fuel.
    my_car = Car(100, "limo")

    # Add 20 more units of fuel to this new car object using the add method.
    my_car.add_fuel(20)

    print(f"{my_car.name} has fuel:{my_car.fuel}")

    my_car.drive(115)

    print(my_car)


if __name__ == "__main__":
    main()


