class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_Details(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")

class Electronic_Product(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_Details(self):
        super().display_Details()
        print(f"Warranty: {self.warranty} months")

e1 = Electronic_Product("HP", 200000, 6)
e1.display_Details()
