# core component
class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Simple coffee"

# base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()

# concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", with milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", with sugar"

class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3

    def description(self):
        return self._coffee.description() + ", with whipped cream"

# client code
def coffee_shop():
    print("Welcome to the Coffee Shop!")
    print("Base coffee: $5")
    print("Add-ons: Milk ($2), Sugar ($1), Whipped Cream ($3)\n")

    coffee = Coffee()

    while True:
        print(f"\nYour current order: {coffee.description()}")
        print(f"Total cost: ${coffee.cost()}")

        print("\n1. Add Milk")
        print("2. Add Sugar")
        print("3. Add Whipped Cream")
        print("4. Finish order")

        choice = input("Enter your choice: ")

        if choice == "1":
            coffee = MilkDecorator(coffee)
        elif choice == "2":
            coffee = SugarDecorator(coffee)
        elif choice == "3":
            coffee = WhippedCreamDecorator(coffee)
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

    print("\nFinal Order Details:")
    print(f"Order: {coffee.description()}")
    print(f"Total Cost: ${coffee.cost()}")
    print("Thank you for your order!")


if __name__ == "__main__":
    coffee_shop()