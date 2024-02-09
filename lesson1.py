# # ООП - Объектно Ориентрованное Программирование
# # DRY - Don`t repeat yourself == не повторяй себя

# class Car: # чертеж
#     #  __init__ - Конструктор, инструкция
#     # self - сам объект
#     # self.brand = атрибут/поле/свойства объекта
#     def __init__(self, brand, year, color):
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.wheels = 4
#         self.is_start = False
#         self.tank = 0

#     def info(self):
#         print(f"Бренд - {self.brand}, \nгод выпуска - {self.year}, \nцвет - {self.color}\n")

#     def start(self):
#         self.is_start = True
#         print("Машина завелась")

#     def drive(self):
#         if self.is_start == True and self.tank>0:
#             print(f"Машина {self.brand} поехала")
#         else:
#             print("С начала заваедите машину или пополните бак")

#     def stop(self):
#         self.is_start = False
#         print("Машина остановилась")

#     def fill_up(self, petrol):
#         self.tank += petrol
#         print(f"Вы заполниди бак на {petrol} литров")

#     # def drive(self, speed):
#     #     print(f"машина {self.brand} едет со скоростью {speed} км\ч")


# bmw = Car("bmw - m5 f90", 2019, "Матовый") # экземпляр / объект класса
# mers = Car("mersedes - e63s", 2023, "Белый")
# tesla = Car("tesla  - model x", 2020, "Black")
# bently = Car("bently", 2002, "Розовый")

# bmw.info()
# bmw.fill_up(50)
# bmw.start()
# bmw.drive()
# bmw.stop()
# bmw.drive(60)
# mers.info()
# tesla.info()

# class Animal:
#     def __init__(self, breed, color):
#         self.breed = breed
#         self.color = color

#     def info_about_animal(self):
#         print(f"Порода - {self.breed} и цвет - {self.color}")

# class Dog(Animal):
#     def __init__(self, breed, color, name):
#         super().__init__(breed, color)
#         # Animal.__init__(self, breed, color)

#         self.name = name

#     def info_about_animal(self):
#         print(f"Имя - {self.name} Порода - {self.breed} и цвет - {self.color}")

# dog = Dog("алабай", "Белый", "Rex")
# dog.info_about_animal()


class Cars :
    def __init__(self, model, year , color):
        self.model = model
        self.year = year
        self.color = color
        self.fuel = 0

    def refuel (self):
       while True:
            if self.fuel < 40:
              self.fuel += 10
            else:
               print (f" бак за раз можно пополнит на 40 литров")
               break


    def drive(self):
        city = input ("введите называние города :")
        distance = float(input("введите растояние до города "))
        need = distance / 10  

        if need <= self.fuel: 
            self.fuel -= need
            print (f"машина {self.model} {self.year} года , {self.color} цвета едет в город {city}")
            print (f"пройдено {distance} km,")
        else :
            r_distance = self.fuel * 10
            print (f"машина не может доехат до города")
            print (F"машина может проехат {r_distance} kmh на текушем баке")

iman = Cars(model = "amg" , year = "2005" , color = "black")
iman.refuel()
iman.drive()

  