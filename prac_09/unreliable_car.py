from car import Car
from random import randint


class UnreliableCar(Car):
    """A specialized version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Construct an UnreliableCar object with a name, fuel, and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance based on its reliability."""
        random_number = randint(1, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven


