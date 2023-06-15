'''
House class representing the complex object we want to create (a house). We also have an abstract HouseBuilder class with methods for building 
different parts of the house and retrieving the final house. The BasicHouseBuilder and FancyHouseBuilder classes extend the HouseBuilder class 
and implement the specific building logic for each type of house.

The HouseDirector class is responsible for orchestrating the building process. It takes a builder object in its constructor and uses it to 
build the house step by step.

The client code creates instances of the BasicHouseBuilder and FancyHouseBuilder. It then sets the builder for the director, constructs the 
house using the director, and retrieves the final house from the builder. The resulting houses are printed.

Using this approach, you can easily create different types of houses (e.g., basic or fancy) by defining different builder classes. The 
construction process is flexible, allowing you to customize and vary the building steps as needed while keeping

'''

class House:
    def __init__(self):
        self.foundation = None
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None

    def __str__(self):
        return f"Foundation: {self.foundation}, Walls: {self.walls}, Roof: {self.roof}, Windows: {self.windows}, Doors: {self.doors}"


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        pass

    def build_walls(self):
        pass

    def build_roof(self):
        pass

    def build_windows(self):
        pass

    def build_doors(self):
        pass

    def get_house(self):
        return self.house


class BasicHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "Basic foundation"

    def build_walls(self):
        self.house.walls = "Basic walls"

    def build_roof(self):
        self.house.roof = "Basic roof"

    def build_windows(self):
        self.house.windows = "Basic windows"

    def build_doors(self):
        self.house.doors = "Basic doors"


class FancyHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "Fancy foundation"

    def build_walls(self):
        self.house.walls = "Fancy walls"

    def build_roof(self):
        self.house.roof = "Fancy roof"

    def build_windows(self):
        self.house.windows = "Fancy windows"

    def build_doors(self):
        self.house.doors = "Fancy doors"


class HouseDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_foundation()
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_windows()
        self.builder.build_doors()


# Usage
basic_builder = BasicHouseBuilder()
fancy_builder = FancyHouseBuilder()

director = HouseDirector(basic_builder)
director.construct_house()
basic_house = basic_builder.get_house()
print("Basic House:")
print(basic_house)

director = HouseDirector(fancy_builder)
director.construct_house()
fancy_house = fancy_builder.get_house()
print("Fancy House:")
print(fancy_house)
