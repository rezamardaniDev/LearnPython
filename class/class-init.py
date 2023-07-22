class Car:
    def __init__(self, color, model) -> None:
        self.color = color
        self.model = model

    def pritnter(self):
        print(f"{self.color} : {self.model}")

car1 = Car("red", "bmw")
car1.pritnter()