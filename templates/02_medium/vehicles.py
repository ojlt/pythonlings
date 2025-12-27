"""
Vehicle Class Hierarchy

You are tasked with implementing a class hierarchy for vehicles.

1. Vehicle (Base Class):
   - Implement the __init__(self, make, model, year).
   - Implement a method get_info(self) that returns a string:
     "{year} {make} {model}".
   - Implement a method refuel(self) that returns the string "Refueling...".

2. Car (Subclass of Vehicle):
   - Implement the __init__(self, make, model, year, num_doors). It should
     call the parent constructor.
   - Override the get_info(self) method to return a string:
     "{year} {make} {model} ({num_doors} doors)".

3. ElectricCar (Subclass of Car):
   - Implement the __init__(self, make, model, year, num_doors, battery_range).
     It should call the parent constructor.
   - Override the get_info(self) method to return a string:
     "{year} {make} {model} ({num_doors} doors) - {battery_range}km range".
   - Override the refuel(self) method to return the string "Recharging...".

Examples:
    v = Vehicle("Honda", "CR-V", 2022)
    v.get_info() -> "2022 Honda CR-V"
    v.refuel() -> "Refueling..."

    c = Car("Toyota", "Camry", 2023, 4)
    c.get_info() -> "2023 Toyota Camry (4 doors)"
    c.refuel() -> "Refueling..."

    e = ElectricCar("Tesla", "Model 3", 2024, 4, 500)
    e.get_info() -> "2024 Tesla Model 3 (4 doors) - 500km range"
    e.refuel() -> "Recharging..."
"""

# I AM NOT DONE


class Vehicle:
    pass


class Car(Vehicle):
    pass


class ElectricCar(Car):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_vehicle():
    v = Vehicle("Honda", "CR-V", 2022)
    assert v.get_info() == "2022 Honda CR-V"
    assert v.refuel() == "Refueling..."


def test_car():
    c = Car("Toyota", "Camry", 2023, 4)
    assert c.get_info() == "2023 Toyota Camry (4 doors)"
    assert c.refuel() == "Refueling..."


def test_electric_car():
    e = ElectricCar("Tesla", "Model 3", 2024, 4, 500)
    assert e.get_info() == "2024 Tesla Model 3 (4 doors) - 500km range"
    assert e.refuel() == "Recharging..."


def test_inheritance():
    e = ElectricCar("Tesla", "Model 3", 2024, 4, 500)
    assert isinstance(e, ElectricCar)
    assert isinstance(e, Car)
    assert isinstance(e, Vehicle)


if __name__ == "__main__":
    test_vehicle()
    test_car()
    test_electric_car()
    test_inheritance()
    print("All tests passed!")
