                                #    Домашняя работа №3

# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.

# 2. Добавить в класс Computer приватный метод make_computations, в котором бы выполнялись арифметические
#  вычисления(‘+’,  ‘-’,  ‘*’,  ‘/’ ) с атрибутами объекта cpu и memory результат вывести красиво с помощью ‘ f ’ .

# 3. Добавить геттеры к существующим атрибутам.


class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    
    @property
    def get_cpu(self):
        return self.__cpu
    
    @property
    def get_memory(self):
        return self.__memory

    def __make_computations(self, operation):
        if operation not in ['+', '-', '*', '/']:
            result = None
        
        if operation == '+':
            result = self.__cpu + self.__memory
            print(f'Результат сложения: {result}')
        
        elif operation == '-':
            result = self.__cpu - self.__memory
            print(f'Результат вычитания: {result}')
        
        elif operation == '*':
            result = self.__cpu * self.__memory
            print(f'Результат умножения: {result}')
        
        elif operation == '/':
            result = self.__cpu / self.__memory
            print(f'Результат деления: {result}')
            
        else:
             print(f"Результаты вычислений ({self.__cpu} {operation} {self.__memory}): {result}")

    
    @property
    def get_make_computations(self):
        return self.__make_computations


computer = Computer(6,8 )
print(f"CPU: {computer.get_cpu}, Memory: {computer.get_memory}")

computer.get_make_computations('+')
computer.get_make_computations('-')
computer.get_make_computations('*')
computer.get_make_computations('/')


# 4. Создать класс Laptop - который наследуется от класса Computer с приватным полем memory_card(карта памяти)
# 5. Добавить геттеры к существующему атрибуту.
# 6. Распечатать информацию о созданных объектах с помощью метода info
# 7. Опробовать все возможные методы каждого объекта

class Laptop (Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    @property
    def get_memory_card(self):
            return self.__memory_card
    
    def info(self):
        print(f"СPU - {self.get_cpu}, Memory - {self.get_memory}, карта памяти - {self.get_memory_card}")

laptop = Laptop(12,21,23)
laptop.get_make_computations('+')
laptop.get_make_computations('-')
laptop.info()
laptop1 = Laptop(16,21,56)
laptop1.get_make_computations('*')
laptop1.get_make_computations('/')
laptop1.info()




# 2 .  ВАРИАНТ 
# class Computer:
#     def __init__ (self, cpu, memory):
#         self.__cpu = cpu
#         self.__memory = memory

#     @property
#     def get__cpu(self):
#         return self.__cpu
#     @property
#     def get__memory(self):
#         return self.__memory

#     def __make_computations(self):
#         print (f"сложение - {self.__cpu + self.__memory} вычитание  {self.__cpu -  self.__memory}")
#         print (f"умножение - {self.__cpu * self.__memory} деление - {self.__cpu / self.__memory}")
    
         
#     @property
#     def get__make_computations(self):
#             return self.__make_computations
    
# computer = Computer( 10, 12)
# computer.get__make_computations()

