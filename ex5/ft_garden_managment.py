class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class HealthError(GardenError):
    pass


class GardenManager:
    @staticmethod
    def add_plants(plants: list) -> None:
        for plant in plants:
            if plant == "" or plant is None:
                raise PlantError("Plant name cannot be empty")
            else:
                print(f"Added {plant} successfully")

    @staticmethod
    def water_plants(plant_list: list) -> None:
        print("Opening watering system")
        try:
            for plant in plant_list:
                try:
                    if plant is None:
                        raise TypeError("Cannot water None - invalid plant!")
                    print(f"Watering {plant} - success")
                except TypeError as e:
                    print(f"Error processing plant: {e}, "
                          f"skipping to next plant...")

        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant_name: str, water_level: int,
                           sunlight_hours: int) -> None:
        if plant_name == "" or plant_name is None:
            raise HealthError("Plant name cannot be empty!")
        elif water_level > 10:
            raise HealthError(f"{plant_name}: Water level {water_level} "
                              f"is too high (max 10)")
        elif water_level < 1:
            raise HealthError(f"{plant_name}: Water level {water_level} "
                              f"is too low (min 1)")
        elif sunlight_hours < 2:
            raise HealthError(f"{plant_name}: Sunlight hours {sunlight_hours} "
                              f"is too low (min 2)")
        elif sunlight_hours > 12:
            raise HealthError(f"{plant_name}: Sunlight hours {sunlight_hours} "
                              f"is too high (max 12)")
        else:
            print(f"{plant_name}: healthy (water: {water_level},"
                  f" sun: {sunlight_hours})")


def test_garden_managment() -> None:
    print("=== Garden Managment System ===\n")
    print("Adding plants to garden...")
    try:
        GardenManager.add_plants(["tomato", "lettuce", ""])
    except PlantError as e:
        print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    try:
        GardenManager.water_plants(["tomato", "lettuce", None, "orange"])
    except WaterError as e:
        print(f"Error watering plant: {e}")
    print("\nChecking plant health...")
    try:
        GardenManager.check_plant_health("tomato", 5, 8)
        GardenManager.check_plant_health("lettuce", 15, 5)
    except HealthError as e:
        print(f"Error checking {e}")
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_managment()
