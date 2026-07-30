# num = int(input("Enter a number: "))
# print(100/num)

# try:
#     num = int(input("Enter a number: "))
#     print(100/num)
# except ZeroDivisionError:
#     print("Cannot divide by Zero")
# except ValueError:
#     print("Please enter a valid number!")
# else:
#     print("Division Successful!")
# finally:
#     print("Program Finished!")

try:
    age = int(input("Enter your age: "))
    if age < 0:
       raise ValueError("Enter valid age")
    print(age)
except ValueError:
    print("Please enter a valid number!")
else:
    print("Age accepted!")
finally:
    print("Program Finished!")
