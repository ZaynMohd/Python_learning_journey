#1 file = open("notes.txt","w")
# file.write(
#     "Name : Zain\n")
# file.write(
#     "Course : Data Science\n")
# file.write(
#     "College : Lords Institute of Engineering and Technology\n"
# )
# file.close()

#2 file = open("notes.txt","r")
# content = file.read()
# print(content)
# file.close()

#3 file = open("notes.txt","r")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

#4 file = open("notes.txt","r")
# line1 = file.readline()
# print(line1)
# file.close()

# file = open("notes.txt")
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()
# file.close()

file = open("notes.txt","r")
lines = file.readlines()
for line in lines:
    print(line, end="")
file.close()