class Car:
    def __init__(self, model, speed, color):
        self.model = model
        self.speed = speed
        self.color = color

my_car = Car("toyota", 220, "red")

print(f"my car's color is {my_car.color}") 