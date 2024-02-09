
#     # магические действия для арифметических действий 
 
    # def add__(self, other): #
    #     __add == сложение ("+") 
    #     new_year =  self.year + other.year 
    #     return Car(self.model, new_year, self.wheels) 
     
    # def sub__(self, other): #
    #     __sub == вычитание ("-") 
    #     new_wheels =  self.wheels - other.wheels 
    #     return Car(self.model, self.year ,new_wheels) 
 
    # def mul__(self, other): #
    #     __mil == Умножение ("*") 
    #     new_wheels =  self.wheels * other.wheels 
    #     return Car(self.model, self.year ,new_wheels) 
     
    # def floordiv__(self, other): 
    #     __floordiv == деление ("//") 
    #     new_wheels =  self.wheels // other.wheels 
    #     return Car(self.model, self.year ,new_wheels) 
     
    # def bool__(self, other): 
    #     __floordiv == деление ("//") 
    #     new_wheels =  self.wheels // other.wheels 
    #     return Car(self.model, self.year ,new_wheels) 


#      # Магические методы для операторов сравнения 
 
#     def __gt__(self, other): 
#        return self.year > other.year 
#     def __lt__(self, other): 
#        return self.year < other.year 
        
#     def __eq__(self,other): 
#        return self.year == other.year 
     
#     def __ne__(self,other): 
#        return self.year != other.year 
#     def __ge__(self,other): 
#        return self.year >= other.year 
#     def __le__(self,other): 
#        return self.year <= other.year 
 
# car1 = Car("BMW - f90", 2021, 4) 
# car2 = Car("BMW - f6", 2023, 4)  
 
# # Арифметические действия  
# print(car1+car2) 
# print(car1-car2) 
# print(car1*car2) 
# print(car1//car2) 
#  # car.info() #Если вызвать без магического метода выйдет путь 
 
 
# # операторы сравнения 
# print(car1>car2) # Больше чем ">" 
# print(car1<car2) # Меньше чем "<" 
# print(car1==car2) # Равно "==" 
# print(car1!=car2) # Неравняется "!=" 
# print(car1>=car2) # Больше или равно ">" 
# print(car1<=car2) # Меньше или равно ">" 
 

# Elizar, [20.01.2024 13:54]
# Множественное наследование# class Car:


# class Car:
   
#     def __init__(self, model, year):          
#         self.model = model
#         self.year = year
#     def info(self):        
#          print(f"Бренд машины - {self.model}, год выпуска - {self.year}")
# class ElectricCar(Car):
#     def __init__(self, model, year, battery):         
#         Car.__init__(self, model, year)
#         self.battery = battery
#     def drive(self):         
#          print(f"{self.model}, едет на электричестве")
    
# class FuelCar(Car):     
#     def __init__(self, model, year, fuel_bank):
#         Car.__init__(self, model, year)        
#         self.fuel_bank = fuel_bank
#     def drive(self):
#         print(f"{self.model}, едет на Топливо!")
# class HybridCar(ElectricCar, FuelCar):    
#     def __init__(self, model, year,  fuel_bank, battery,):
#         FuelCar.__init__(self, model, year, fuel_bank)        
#         ElectricCar.__init__(self, model, year, battery)
#     def drive(self):
#         print(f"{self.model}, едет на Топливо! и на электричечтве")
# tesla = ElectricCar("Tesla Model X", 2022, 150000)
# tesla.info()
# tesla.drive()
# audi = FuelCar("Rs-8", 2018, 15) 
# audi.info()
# audi.drive()
# toyota = HybridCar("Avalon", 2023, 100000, 10)
# toyota.info()
# toyota.drive()


class Car: 
    def __init__(self, model, year): 
        self.model = model 
        self.year = year           
         
    def __str__(self): 
        return f"Модель - {self.model}, Год выпуска - {self.year}" 
     
         # def __call__(self): 
    #     print("hello call") 


    def __add__(self, other): 
        res = self.year + other.year 
        return Car(self.model, res) 
     
         
    def __sub__(self, other): 
        res = self.year - other.year 
        return Car(self.model, res) 
     
             
    def __mul__(self, other): 
        res = self.year * other.year 
        return Car(self.model, res) 
     

    def __floordiv__(self, other):
        res = self.year // other.year
        return Car (self.model, res)
     
    def __truediv__(self, other):
        res = self.year / other.year
        return Car (self.model, res)
     
     # магические методы для  операторов сравнение

    def __gt__ (self,other):
        return self.year > other.year

    def __gt__ (self,other):
        return self.year < other.year
      
    def __eg__ (self,other):#ровно equals
        return self.year == other.year

    def __ne__(self,other): 
        return self.year != other.year 
    
    def __ge__(self,other):  # больше или ровно 
        return self.year >= other.year 

    def __le__(self,other):  # меньше или ровно 
        return self.year <= other.year 


# "= "  - это знак присываение 
# "==" знак равонство
    


bmw = Car("BMW - m5", 2022) 
mers = Car("BMW - m5", 2023) 
 
# print(bmw * mers) 
# print( bmw + mers)
# print(bmw *mers) 
# print(bmw // mers) 
print (mers)
print(bmw)

  # магические методы для  операторов сравнение

print(bmw>mers)
print(bmw<mers)
print (mers == bmw)