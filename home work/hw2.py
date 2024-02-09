#                                  Домашняя работа №2

# 1. Создать класс Person с атрибутами fullname, age, is_married
# 2. Добавить в класс Person метод introduce_myself(представиться), который бы распечатывал всю информацию о человеке
# 3. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
# 4. Добавить в класс Teacher атрибут класса salary
# 5. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле:
# к стандартной зарплате прибавляется бонус 3000 за каждый год опыта.
# 6. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату


# class Person:
#     def __init__ (self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married
   
#     def introduce_myself (self):
#         print(f" my name is - {self.fullname} , and i am - {self.age}, and iam {self.is_married}")

# person = Person("iman" , "21" , "not married")  
# person.introduce_myself()

# class Teacher(Person):
#     def __init__ (self, fullname, age, is_married, experience):
#         Person.__init__(self, fullname, age, is_married,)
#         self.experience=experience
#         self.salary = 50000

#     def salary_card(self):
#         for i in range(self.experience):  
#             self.salary +=3000
#         print(f"{self.fullname}, ваша зарплата СОСТОВЯЛАЕТ В ЭТОМ МЕСЯЦЕ: {self.salary}")  


# teacher = Teacher('IMAN', 21, 'not', 4)
# teacher.salary_card()

               #   ПОВТОРНЫЙ 

class Person:
    def __init__ (self, fullname, age , is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def inproduce_my_self(self):
        print(f"{self.fullname},- {self.age},- {self.is_married}")
person = Person("my name is IMAN",  "i am 21", "not married")
person.inproduce_my_self()


class Teacher(Person):
    def __init__ (self, fullname, age , is_married, experience):
        Person.__init__ (self, fullname, age, is_married)
        self.experience = experience
        self.salary = 50000

    def salary_card (self):
        for i in range (self.experience):
            self.salary += 3000
            print (f"{self.fullname} ваша зарплата составляет в этом  месяце {self.salary}")

teacher = Teacher ('ZHOROEEVV' , 21, 'not',  5)
teacher.salary_card()
