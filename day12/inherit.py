# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     pass
# dog = Dog()
# dog.sound()

#2 class Animal:
#     def sound(self):
#         print("Animal Sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")  #method overriding is used

# dog = Dog()
# dog.sound()

#3 class Animal:
#      def eat(self):
#          print("Animal is eating")
#      def sleep(self):
#           print("Animal is sleeping")
# class Dog(Animal):
#      def bark(self):
#          print("Dog is barking")
#      def eat(self):
#           print("Dog is eating")
# dog = Dog()
# dog.eat()
# dog.bark()
# dog.sleep()
# class Cat(Animal):
#      def meow(self):
#           print("Cat is meowing")
# cat = Cat()
# cat.eat()
# cat.meow()
# cat.sleep()


#4 class Animal:
#     def __init__(self, name):
#         self.name = name
# class Dog(Animal):
#     def bark(self):
#         print(self.name, "is barking")
# dog = Dog("Bruno")
# dog.bark()

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def bark(self):
        print(self.name,"is a", self.breed, "and is barking")
dog = Dog("Bruno", "Labrador")
dog.bark()

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def meow(self):
        print(self.name,"is a", self.breed, "and is meowing")
cat = Cat("Kitty", "Persian")
cat.meow()

class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def fly(self):
        print(self.name,"is a", self.color, "and is flying")
bird = Bird("Tweety", "Yellow")
bird.fly()
        