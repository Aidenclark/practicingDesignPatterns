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

'''
The House class represents a house and stores the values for its foundation, walls, roof, windows, and doors. 
The __str__ method returns a string representation of the house.
'''


class House:
    def __init__(self):
        self.foundation = None  # Represents the foundation of the house
        self.walls = None  # Represents the walls of the house
        self.roof = None  # Represents the roof of the house
        self.windows = None  # Represents the windows of the house
        self.doors = None  # Represents the doors of the house

    def __str__(self):
        return f"Foundation: {self.foundation}, Walls: {self.walls}, Roof: {self.roof}, Windows: {self.windows}, Doors: {self.doors}"
'''
The HouseBuilder class is an abstract class that provides a blueprint for building a house.
It initializes an instance of House to represent the house being built.
The build_foundation, build_walls, build_roof, build_windows, and build_doors methods are placeholders that need to be implemented in subclasses to define how to build each part of the house.
The get_house method returns the built house.
'''

class HouseBuilder:
    def __init__(self):
        self.house = House()  # Represents the house being built

    def build_foundation(self):
        pass  # Placeholder method to build the foundation

    def build_walls(self):
        pass  # Placeholder method to build the walls

    def build_roof(self):
        pass  # Placeholder method to build the roof

    def build_windows(self):
        pass  # Placeholder method to build the windows

    def build_doors(self):
        pass  # Placeholder method to build the doors

    def get_house(self):
        return self.house  # Returns the built house
''''
The BasicHouseBuilder class is a subclass of HouseBuilder and provides the implementation to build a basic house.
It overrides the placeholder methods to define how to build each part of a basic house.
''''
class BasicHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "Basic foundation"  # Builds a basic foundation

    def build_walls(self):
        self.house.walls = "Basic walls"  # Builds basic walls

    def build_roof(self):
        self.house.roof = "Basic roof"  # Builds a basic roof

    def build_windows(self):
        self.house.windows = "Basic windows"  # Builds basic windows

    def build_doors(self):
        self.house.doors = "Basic doors"  # Builds basic doors


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

'''
The HouseDirector class is responsible for constructing a house using a specific builder.
It takes a builder as a parameter in the constructor to specify which builder to use.
The construct_house method orchestrates the construction process by calling the builder's methods in the appropriate order.
'''
class HouseDirector:
    def __init__(self, builder):
        self.builder = builder  # Represents the builder to use

    def construct_house(self):
        self.builder.build_foundation()  # Builds the foundation
        self.builder.build_walls()  # Builds the walls
        self.builder.build_roof()  # Builds the roof
        self.builder.build_windows()  # Builds the windows
        self.builder.build_doors()  # Builds the doors


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


'''
When defining a method inside a class, the first parameter of the method is typically self. This parameter is automatically passed when you call a method 
on an instance of the class. By convention, self is used as the name for this parameter, but you can technically choose any valid variable name.

The self parameter allows you to access and manipulate the attributes of the instance from within its methods. It provides a way to maintain the state of 
the object and perform actions related to that instance.


---


In Python, the pass statement is a placeholder that does nothing. It is used when a statement is syntactically required but you don't want to perform any 
actions or add any code at that point.

In the context of the Builder design pattern code example provided earlier, pass is used as a placeholder within the build_* methods of the HouseBuilder 
and its subclasses. The intention is to indicate that these methods should be implemented in the subclasses with the specific building logic for each part 
of the house

'''
