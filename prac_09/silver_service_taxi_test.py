from silver_service_taxi import SilverServiceTaxi


class Taxi(SilverServiceTaxi):
    """A specialized version of a Car that includes fare costs."""
    price_per_km = 1.23

    def __init__(self, name, fuel):
        """Initialize a Taxi instance, inheriting from the SilverServiceTaxi class."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string representation of the Taxi, including the current fare distance and price per kilometer."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def calculate_fare(self):
        """Calculate and return the fare for the current trip."""
        return self.price_per_km * self.current_fare_distance

    def reset_fare(self):
        """Reset the fare distance to start a new fare."""
        self.current_fare_distance = 0

    def drive_distance(self, distance):
        """Drive the taxi a certain distance, updating the fare distance accordingly."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


