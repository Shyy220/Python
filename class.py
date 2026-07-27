class student:
    def __init__(self):
        self.__marks=90  #private attribute
    def show(self):
        print("Marks : ", self.__marks)

s = student()
#print(s.__marks) error
s.show()

#Protect data, keep data safe inside the class known as Encapsulation
#Encapsulation means wrapping data and functions together inside a class and controlling access to the data

class Student:
    def __init__(self):
        self.__marks = 90

    def set_marks(self,new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
    def show_marks(self):
        print("Marks:", self.__marks)

s = Student()
s.show_marks()

s.set_marks(95)
s.show_marks()

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student Name: " +self.name

