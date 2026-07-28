#1 class Student:
#     pass
# s1 = Student()
# s2 = Student()
# print(s1)
# print(s2)

#2 class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Zain", 20)
# print(s1.age)
# print(s1.name)

#3 class Student:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("Hello",self.name)

# s1 = Student("Zain")
# s1.greet()

class Student:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
s1 = Student("Zain")
print(s1.name)

s1.change_name("Ahmed") #updating the name here
print(s1.name)