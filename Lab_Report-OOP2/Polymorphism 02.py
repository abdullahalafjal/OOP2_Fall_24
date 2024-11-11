class Transport:
    def calculate(self, weight, distance):
        raise NotImplementedError("Implement this method")


class Truck(Transport):
    def calculate(self, weight, distance):
        return 3 * weight + 4 * distance


class Ship(Transport):
    def calculate(self, weight, distance):
        return 5 * weight + 3 * distance


class Plane(Transport):
    def calculate(self, weight, distance):
        return 10 * weight + 6 * distance


def calculate_delivery_cost(transports, weight, distance):

    for i in transports:
        cost = i.calculate(weight, distance)
        print(f"{i.__class__.__name__} delivery cost: ${cost:.2f}")


truck = Truck()
ship = Ship()
plane = Plane()

transports = [truck, ship, plane]

calculate_delivery_cost(transports, weight=100, distance=85)
