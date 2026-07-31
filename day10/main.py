import calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice - in numbers: "))



try:
  if choice == 1:  
    print("Addition: ",calculator.add(num1, num2))
  elif choice == 2:
    print("Subtraction: ",calculator.subtract(num1, num2))
  elif choice == 3:
    print("Multiplication: ",calculator.multiply(num1, num2))
  elif choice == 4:
    print("Division: ",calculator.divide(num1, num2))
  else:
    print("Invalid choice")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter only numbers")
