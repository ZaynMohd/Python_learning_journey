# numbers = [1,2,3,4,5,6,7,8,9,10]
# sqaures = [num ** 2 for num in numbers]
# even_numbers = [num for num in numbers if num % 2 == 0]
# odds = [num ** 3 for num in numbers if num % 2 != 0]
# print(sqaures)
# print(even_numbers)
# print(odds)

# names = ["zain","ali","sara"]
# upper = [x.upper() for x in names]
# print(upper)

# names = ["zain","ali","mohammed","sara","john"]
# lenghty = [name for name in names if len(name) > 4]
# print(lenghty)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# result = [num ** 3 for num in numbers if num % 3 == 0]
# even = [num for num in numbers if num % 2 == 0]
# print(even)
# print(result)

names = ["zain","ali","mohammed","sara","john"]
results = [name.upper() for name in names if len(name) > 3]
print(results)