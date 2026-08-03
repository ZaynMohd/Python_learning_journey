# class Student:
#     def __init__(self):
#         self.name = "Zain"
# student = Student()
# print(student.name)

# class Student:
#     def __init__(self):
#         self.__name = "Zain" #here we convert the varible into private var
# student = Student()
# print(student.__name) #so if we run this it will display an error

# class Student:
#     def __init__(self):
#         self.__name = "Zain"
# student = Student()
# print(student._Student__name) #this will print the value & it is used to accidental access not for security

# class Bank:
#     def __init__(self):
#         self.__balance = 5000
# account = Bank()
# print(account._Bank__balance)

# class Bank:
#     def __init__(self):
#         self.__balance = 5000
#     def get_balance(self):
#         return self.__balance
#     def deposit(self, amount):
#         self.__balance += amount

# account = Bank()
# account.deposit(2000)
# print(account.get_balance())

class Bank:
    def __init__(self):
        self.__balance = 5000
    def set_balance(self, amount):
        if amount < 0:
            print("Invalid balance")
        else:
            self.__balance = amount
    def get_balance(self):
        return self.__balance

account = Bank()
account.set_balance(-500)
print(account.get_balance())

