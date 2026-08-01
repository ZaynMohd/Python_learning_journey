# class Student:
#     pass
# student1 = Student()
# student2 = Student()

# print(student1)
# print(student2)

#2 class Student:
#     def __init__(self):
#         print("Student object created")

# student1 = Student()
# student2 = Student()

#3 class Student:
#     def __init__(self):
#         print(self) #self always refers the current object

# student1 = Student()
# student2 = Student()

class Student:
    def __init__(self):
        self.name = "Zain"

student1 = Student()
student2 = student1

student2.name = "Ahmed"
print(student1.name)
print(student2.name)