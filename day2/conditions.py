# num=int(input("Enter a number:"))
# if num >= 10:
#     print("Number is 10 or great")
# else:
#     print("Number is less than 10")
#  num = int(input("Enter the marks: "))
#  if num > 100 or num < 0:
#      print("Invalid Marks")
#  elif num >= 90:
#      print("Grade A")
#  elif num >= 70:
#      print("Grade B")
#  elif num >= 50:
#      print("Grade C")
#  elif num >= 40:
#      print("Grade D")
#  else:
#       print("Fail")
correct_username = "zain"
correct_password = "python123"
username = input("Enter the username: ")
password = input("Enter the password: ")
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid username or password")