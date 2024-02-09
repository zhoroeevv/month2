#                        Домашнее Задание 
# Задание 1:
# Создайте класс Fruits c атрибутами - (name, color, weight)
# Создайте три объекта класса и с помощью метода выведите информацию о каждом фрукте

class Fruits :
    def __init__(self, name , color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    def info_about_fruits(self):
        print (f"{self.name} цвет - {self.color} масса - {self.weight}")

fruits = Fruits ("яблоко" , "красное " , "40kg")
fruits.info_about_fruits()




#                                 Задание 2:
# Создайте класс Car c атрибутами - (model, year, color)
# Создайте метод drive с входящим параметром city(город) который будет выводить текст 
# (Машина - `модель вашей машины`  едет в  - `ваш город`)



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
               print (f" бак за раз можно заполнит на 40 литров")
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

iman = Cars( model =  "AMG W211 5.5" , year = "2002" , color = "PHANTOM") 
iman.refuel()
iman.drive()

  
                                        # Доп. Задание: