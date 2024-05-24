class Vehicle:
    def __init__ (self, model, make):
        self.model = model
        self.make = make


class Bus(Vehicle):
    def __init__ (self, model, make, capacity):
        super().__init__ (model, make)
        self.capacity = capacity


    def hoot(self):
            print("THe bus is hooting")


    def check_capacity(self):
            print("The capacity is {self.capacity}")


class Lorry(Vehicle):
    def __init__ (self, model, make, load_weight):
        super().__init__ (model, make)
        self.load_weight = load_weight
    def unload(self):
            print("Unloading the lorry")
b = Bus("x", "Isuzu", 70)
b.model()
b.hoot()
l = Lorry("T", "Scania", 1000)
l.model()
l.hoot()

