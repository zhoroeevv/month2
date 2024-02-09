# Основные принципы ООП

class Animals: # Родителоьский класс и Абстрактный класс
    def __init__(self, breed, classes, color, age):
        self.breed = breed
        self.classes = classes
        self.color = color
        self.age = age

    def info(self):
        print(f"{self.breed}, {self.classes}, {self.color}, {self.age}")

class Dog(Animals): # Дочерний класс
    def __init__(self, breed, classes, color, age):
        super().__init__(breed, classes, color, age)
        self.paws = 4

    def info(self):
        print(f"{self.breed}, {self.classes}, {self.color}, {self.age}, кол-во лап-{self.paws}")

    def make_sound(self):
        print("Gaf-Gaf")


class Cat(Animals): # Дочерний класс
    def __init__(self, breed, classes, color, age):
        super().__init__(breed, classes, color, age)
        self.paws = 4

    def info(self):
        print(f"{self.breed}, {self.classes}, {self.color}, {self.age}, кол-во лап-{self.paws}")

    def make_sound(self):
        print("Meow")


class Cow(Animals): # Дочерний класс
    def __init__(self, breed, classes, color, age):
        super().__init__(breed, classes, color, age)
        self.horns = 2

    def info(self):
        print(f"{self.breed}, {self.classes}, {self.color}, {self.age}, кол-во рог-{self.horns}")

    def make_sound(self):
        print("Moo")


dog = Dog("Haski", "млекопитающий", "Grey", 3)
dog.make_sound()

cat = Cat("Ryjik", "млекопитающий", "Orange", 1)
cat.make_sound()

cow = Cow("Murka", "млекопитающий", "Black", 15)
cow.make_sound()