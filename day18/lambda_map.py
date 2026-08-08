cube = lambda x: x ** 3
print(cube(4))

#Squaring the elements of list using normal way
# numbers = [1, 2, 3, 4, 5]
# squares = []
# for num in numbers:
#     squares.append(num ** 2)
# print(squares)


#Now using map function
# numbers = [1, 3, 4, 2]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)

# number = [10,20,30,40]
# square = list(map(lambda z: z * 2, number))
# print(square)

#Filter Function
# numbers = [1,2,3,4,5,6,7,8,9,]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# numbers = [10,15,20,25,30,35]
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print(odd_numbers)

# numbers = [5,10,15,20,25]
# result = list(map(lambda x: x * 10, numbers))
# print(result)


# names = ["zain", "ali", "sara"]
# uppercase = list(map(lambda st: st.upper(), names))
# print(uppercase)

numbers = [1,2,3,4,5,6,7,8,9,10]
num1 = list(filter(lambda x: x > 5, numbers))
num2 = list(filter(lambda y: y % 3 == 0, numbers))
num3 = list(filter(lambda z: z % 2 == 0, numbers))
num3 =  list(map(lambda z: z ** 2, num3))
print("Greater than 5: ", num1)
print("Divisible by 3: ", num2)
print("Even Squares: ", num3)