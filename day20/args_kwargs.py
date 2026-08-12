# def add(*numbers):
#     print(numbers)
# add(10,20,30)

# def student(**details):
#     print(details)
# student(name="Zain", age=20, city="Hyderabad")

# def show(**data):
#     print(len(data))
# show(name="Zain", age=20, city="Hyderabad",college="LIET")

# def multiply(*numbers):
#     total = 1
#     for num in numbers:
#         total *= num
#     print(total)
# multiply(2,3,4)

# def students(**details):
#     for key, value in details.items():
#         print(key, ":" ,value)
# students(name="Zain", age=20, city="Hyderabad")

# def average(*numbers):
#     print(sum(numbers)/len(numbers))
# average(10,20,30,40)

# def profile(name, *skills):
#     print("Name: ", name)
#     print("Skills: ", *skills)
# profile(
#     "Zain",
#     "Python",
#     "Canva", 
#     "Data Science"
# )

def report_card(name, *marks, **details):
    print("Name: ",name)
    print("Marks: ",marks)
    print("Average:",round(sum(marks)/len(marks), 2))
    for key, value in details.items():
        print(key,":",value)
report_card(
    "Zain",
    90, 85, 88,
    city="Hyderabad",
    course="Data Science"
)