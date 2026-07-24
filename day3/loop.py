#1 for i in range(2, 21, 2):
#     print(i)

#2 for i in range(10, 0, -1):
#     print(i)

#3num = int(input("Enter any number: "))
#for i in range(1, 11):
#    print(num, "x", i, "=", num * i)
# count = 1

#4 while count <= 5:
#     print(count)
#     count = count+1
# count = 2

#5 while count <= 8:
#     print(count)
#     count += 2
# count = 1

#6 while count <= 10:
#     print(count)
#     count += 1
# count = 
# count = 10

#7 while count >= 1:
#     print(count)
#     count -= 1

#8 for i in range(1, 11):
#     if i == 3:
#         continue
#     if i == 8:
#         break
#     print(i)
num = int(input("Enter a number: "))
for i in range(1, num+1):
    if i % 2 == 0:
        print(i)
        count = 2