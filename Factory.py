from abc import ABC, abstractmethod

class Clothing(ABC):
    def __init__(self, size, color, material="cotton"):
        self.size = size
        self.color = color
        self.material = material

    @abstractmethod
    def wear(self):
        pass

class Shirt(Clothing):
    def wear(self):
        print(f"Wearing a {self.color} {self.size} size shirt!")

class Trousers(Clothing):
    def wear(self):
        print(f"Wearing {self.color} trousers (size: {self.size})")

class Dress(Clothing):
    def wear(self):
        print(f"Wearing a beautiful {self.color} dress (size: {self.size})")

class ClothingFactory:
    @staticmethod
    def create_clothing(clothing_type, size, color, material="cotton"):
        clothing_type = clothing_type.lower()

        if clothing_type == "shirt" or clothing_type == "shirt":
            return Shirt(size, color, material)
        elif clothing_type == "trousers" or clothing_type == "pants":
            return Trousers(size, color, material)
        elif clothing_type == "dress":
            return Dress(size, color, material)
        else:
            raise ValueError(f"Invalid clothing type: {clothing_type}")


if __name__ == "__main__":
    factory = ClothingFactory()
    clothes = [
        factory.create_clothing("shirt", "M", "Blue"),
        factory.create_clothing("Trousers", "XL", "Black", "denim"),
        factory.create_clothing("Dress", "S", "Pink", "silk"),
    ]

    for item in clothes:
        item.wear()