#funtion (def) : write the code once and use it everytime
#1 def greet():
#     print("Hello Zain!")
#     print("Welcome to Python") #we created the greet and stored the values
# greet() #here we are calling the greet which will display the stored value

#2 def greet(name):
#     print("Hello", name)

# greet("Zain")
# greet("Ahmed")

#3 def square(num):
#     print(num * num)
# square(5)

#4 def add(a, b):
#     return (a + b)
# result = add(10, 20)
# print(result)

#5 def average(a, b, c):
#     return(a+b+c)/3
# result = average(10, 20, 30)
# print(result)

#6 def is_even(num):
#    if num%2==0:
#     return "Even"
#    else:
#     return "Odd"
# print(is_even(8))
# print(is_even(7))

#7 def greet(name="Guest"):
#     print("Hello",name)
# greet()
# greet("Zain")

#8 name = "Zain"    #Global variable

# def show():
#     name = "Ahmed"    #Local variable
#     print(name)
# show()
# print(name)


count = 10
def change():
    global count
    count = 20
change()
print(count)