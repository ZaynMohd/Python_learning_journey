import maths
print(maths.square(5))
print(maths.cube(5))

import greetings
greetings.hello("Zain")

import converter
print(converter.cm_to_m(250))
print(converter.kg_to_g(5))

import calculator
print(calculator.add(10,5))
print(calculator.subtract(10,5))
print(calculator.multiply(10,5))
try:
    print(calculator.divide(10,0))
except ZeroDivisionError:
    print("Cannot divide by zero")
