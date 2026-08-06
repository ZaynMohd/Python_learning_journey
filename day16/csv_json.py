# import csv
# with open("day16/students.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row) # this code is for reading from a file

#2 import csv
# with open("day16/students.csv", "w") as file:
#     writer = csv.writer(file)

# writer.writerow(["Name", "Age", "Marks"])
# writer.writerow(["Sahil", 21, 96]) #this is used to enter the values into a file

#3 import csv
# with open("day16/employees.csv","r") as file:
#     reader = csv.reader(file)

#     next(reader) #this will skip the header
#     for row in reader:
#         print("Name: ",row[0])
#         print("Department: ",row[1])
#         print("Salary: ",row[2])
#         print("---------------------")

#4 import csv
# with open("day16/company.csv","w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["ID", "Name", "Role"])
#     writer.writerow([1, "Zain", "Developer"])
#     writer.writerow([2, "Ali", "Designer"])
#     writer.writerow([3, "Ahmed", "Manager"])

#5 import json
# student = {
#     "name" : "Zain",
#     "age" : 21,
#     "course" : "Data Science"
# }
# with open("day16/student.json", "w") as file:
#     json.dump(student, file, indent=4)
# print("JSON file created successfully")

#6 import json
# employee = {
#     "name" : "Ali",
#     "department" : "HR",
#     "salary" : 40000
#     }
# with open("day16/employee.json","w") as file:
#     json.dump(employee, file, indent=4)
# print("File created successfully")


#7 import json
# with open("day16/employee.json","r") as file:
#     employee = json.load(file)
# print("Employee Name:",employee["name"])
# print("Department:",employee["department"])
# print("Salary:",employee["salary"])

import csv
import json
employees = []
with open("day16/employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        employee = {
            "name": row[0],
            "department" : row[1],
            "salary" : row[2]
        }
        employees.append(employee)

with open("day16/employees.json","w") as file:
    json.dump(employees, file, indent=4)
with open("day16/employees.json","r") as file:
    employees = json.load(file)
    for employee in employees:
        print("Name:",employee["name"])
        print("Dept:",employee["department"])
        print("Salary:",employee["salary"])
        print("-" * 25)