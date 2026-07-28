class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def total_marks(self):
        return sum(self.marks)
    def average(self):
        return self.total_marks() / len(self.marks)
    def result(self):
        if self.average() >= 40:
            return "Pass"
        else:
            return "Fail"
    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "Grade - A"
        elif avg >= 75:
            return "Grade - B"
        elif avg >= 60:
            return "Grade - C"
        elif avg >= 40:
            return "Grade - D"
        else:
            return "Fail - F"
    def display(self):
        print("\n-------- Student Report---------")
        print("Name:", self.name)
        print("Roll no: ", self.roll_no)
        print("Marks :", self.marks)
        print("Total :",self.total_marks())
        print("Average :", self.average())
        print("Result :", self.result())
        print("Grade :", self.grade())
n = int(input("Enter number of Students: "))
students = []
for i in range(n):
    name = input("Enter the Student name: ")
    roll_no = input("Enter the roll no: ")
    marks = [
        int(input("Enter the marks_1: ")),
        int(input("Enter the marks_2: ")),
        int(input("Enter the marks_3: "))]
    student = Student(name, roll_no, marks)
    students.append(student)


grades = {
    "Grade - A": 0,
    "Grade - B": 0,
    "Grade - C": 0,
    "Grade - D": 0,
    "Fail - F": 0,
}

for student in students:
    student.display()
    grade = student.grade()
    grades[grade] += 1

print("\n----- Grade Summary -----")
for grade, count in grades.items():
    print(grade, ":", count)
    