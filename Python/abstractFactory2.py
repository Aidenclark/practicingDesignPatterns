# Abstract Factory Interface
class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

# Concrete Factory 1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

# Concrete Factory 2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

# Abstract Product A
class AbstractProductA:
    def useful_function_a(self):
        pass

# Concrete Product A1
class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A1."

# Concrete Product A2
class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A2."

# Abstract Product B
class AbstractProductB:
    def useful_function_b(self):
        pass

# Concrete Product B1
class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B1."

# Concrete Product B2
class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B2."

# Client code
def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    result_a = product_a.useful_function_a()
    result_b = product_b.useful_function_b()

    print(result_a)
    print(result_b)

# Example usage
if __name__ == '__main__':
    factory1 = ConcreteFactory1()
    client_code(factory1)

    factory2 = ConcreteFactory2()
    client_code(factory2)
