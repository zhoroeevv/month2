#                               Домашняя работа №4

#                       Создание системы менторство как в Geeks


# Создайте абстрактный класс GeeksPeople, который имеет общие свойства, такие как name, email и phone, а также общий 
# магический метод __str__(для вывода информации).


class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f" ИМЯ : - {self.name}, Почта - {self.email}, Номер - {self.phone}, "
    

    #  Создайте класс Student, 


#  Студенты могут иметь свойства, такие как student_id и group_where_study, и методы, такие как study. 
# Метод study - выводит информацию в какой группе учиться студент

class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self, name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f"ИМЯ - {self.name} учится в {self.group_where_study} группе")

    def __str__(self):
        return super().__str__() + f"ID - {self.student_id}, Группа {self.group_where_study}"

student = Student("iman", "zhoroeevv@email.com", "777411000", "41100", "14-2b")
print(student)
student.study()


#  Создайте класс Teacher 

# Преподаватели могут иметь свойства, такие как teacher_id и group_where_teach, и методы, такие как teach. 
# Метод teach - выводит информацию какой группе преподает учитель

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone,teacher_id, group_where_teach):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach(self):
        print(f"группа где он преподает- {self.group_where_teach}")

    def __str__(self):
        return super().__str__() + f"ID - {self.teacher_id}, группа - {self.group_where_teach}, "
    

teacher = Teacher ("Syimyk", "Abdykadyrovv@gmail.com", "+ 996 777 911 911", "911", "14-2B")
print(teacher)
teacher.teach()


#  Создайте класс Admin. 

# Администраторы могут иметь свойства, такие как admin_id и методы, такие как create_group. 
# Метод create_group - создает новую группу


class Admin (GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self, name, email, phone)
        self.admin_id = admin_id

    def create_group (self, kurs_name):
        print(f"Админ {self.name} создал группу {kurs_name}")

    def __str__(self):
        return super().__str__() + f"ID - {self.admin_id}"
    
admin = Admin("Nurbolot", "nurbolot@gmail.com", "777 2333 3445", "121212")
admin.create_group("15-1B")

# Создайте класс Mentor. Класс Mentor должен наследовать от обоих классов, Student и Teacher, и должен иметь доступ
# к свойствам и методам обоих этих классов.

# Создайте несколько объектов каждого типа пользователя и продемонстрируйте, как они могут использовать 
# свои уникальные и общие свойства и методы.

class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
        super().__init__(name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone,teacher_id, group_where_teach)

mentor = Mentor("nurai", "nurai@gmail.com", "21545464454", 122123, "12-2B", 455489, "14-2B")
print(mentor)
mentor.study()
mentor.teach()