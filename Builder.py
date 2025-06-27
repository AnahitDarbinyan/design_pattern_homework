class Burger:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def __str__(self):
        return "Your burger has:\n" + "\n".join(f"- {part}" for part in self.parts)


def build_burger():
    print("~~ BURGER BUILDER ~~")
    print("Let's make your dream burger!\n")

    burger = Burger()

    bun = input("Choose bun (regular/sesame/whole wheat): ")
    burger.add(f"{bun} bun")


    patties = input("How many patties? (1-3): ")
    burger.add(f"{patties} patty" + ("s" if int(patties) > 1 else ""))


    toppings = {
        "cheese": False,
        "lettuce": False,
        "tomato": False
    }

    for topping in toppings:
        if input(f"Add {topping}? (y/n): ").lower() == 'y':
            burger.add(topping)


    sauce = input("Choose sauce (ketchup/mayo/mustard/none): ")
    if sauce != "none":
        burger.add(sauce)

    print("\n" + "=" * 20)
    print(burger)
    print("=" * 20 + "\nEnjoy your burger!")

build_burger()