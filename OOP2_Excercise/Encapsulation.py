class Vehicle:
    def __init__(self, color):
        self.color = color

    def VehicleInfo(self):
        print(f"Vehicle Color: {self.color}")


class Taxi(Vehicle):
    def __init__(self, color, model, capacity, variant):
        super().__init__(color)
        self.__model = model
        self.__capacity = capacity
        self.__variant = variant

    def getModel(self):
        return self.__model

    def getCapacity(self):
        return self.__capacity

    def getVariant(self):
        return self.__variant

    def setModel(self, model):
        self.__model = model

    def setCapacity(self, capacity):
        self.__capacity = capacity

    def setVariant(self, variant):
        self.__variant = variant

    def VehicleInfo(self):
        super().VehicleInfo()
        print(f"Model: {self.__model}")
        print(f"Capacity: {self.__capacity}")
        print(f"Variant: {self.__variant}")


t1 = Taxi("Red", "XR", 4, "XYZ")
t2 = Taxi("Blue", "RX", 7, "XYZ")
t1.VehicleInfo()
t2.VehicleInfo()
