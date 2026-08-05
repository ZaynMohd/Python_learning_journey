#practice
# state = "Tamil Nadu"
# if state.endswith("Nadu"):
#     print("Chennai")
# elif state.startswith("Tamil"):
#     print("Madurai")
# else:
#     print("Hyderabad")

#1 from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# dog = Dog()
# cat = Cat()
# dog.sound()
# cat.sound()


#2 from abc import ABC, abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class UPI(Payment):
#     def pay(self):
#         print("Payment successful through UPI")
# class CreditCard(Payment):
#     def pay(self):
#         print("Payment successful through Credit Card")

# upi = UPI()
# credit = CreditCard()
# upi.pay()
# credit.pay()

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        print(f"Area of Square:  {self.side * self.side}") 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("Area of Circle: ", 3.14 * self.radius * self.radius)

square = Square(5)
circle = Circle(5)
square.area()
circle.area()