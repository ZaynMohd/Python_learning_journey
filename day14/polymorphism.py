# class Dog:
#     def sound(self):
#         print("Woof Woof")

# class Cat:
#     def sound(self):
#         print("Meow Meow")

# class Bird:
#     def sound(self):
#         print("Chirp Chirp")

# dog = Dog()
# cat = Cat()
# bird = Bird()
# dog.sound()
# cat.sound()
# bird.sound()

#2 class Animal:
#     def sound(self):
#         print("Animal makes sounds")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# class Cow(Animal):
#     def sound(self):
#         print("Moo Moo")

# def make_sound(animal):
#     animal.sound()
# dog =Dog()
# cat = Cat()
# cow = Cow()

# make_sound(dog)
# make_sound(cat)
# make_sound(cow)

class Car:
    def __init__(self, brand):
        self.brand = brand
    def drive(self):
        print("self.brand is driving")
class BMW(Car):
    def drive(self):
        print("BMW is driving fast")
class Tesla(Car):
    def drive(self):
        print("Tesla is driving silently")

def start(car):
    car.drive()

bmw = BMW("BMW")
tesla = Tesla("Tesla")

start(bmw)
start(tesla)