#1 languages = ["Python","Java","C++","Javascript"]
# print(languages[2])

#2 subjects = ["Maths","Physics","Chemistry"]
# subjects[1] = "Python"
# subjects.append("AI")
# subjects.remove("Chemistry")
# print(subjects)

#3 colors = ["Red","Blue","Green"]
# colors.insert(1, "Yellow")
# colors.pop(3)
# print(len(colors))
# print(colors)

#4 skills = ["Python","Figma","Github"]
# for skill in skills:
#     print(skill)

marks = [78, 92, 35, 67, 88]
print(sum(marks))
print(len(marks))
print(sum(marks) / len(marks))
print(max(marks))
print(min(marks))
for mark in marks:
    if mark >= 40:
        print("Pass")
    else:
        print("Fail")