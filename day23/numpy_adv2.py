# import numpy as np
# arr = np.array([10,20,30,40,50])
# print(arr[arr > 30])  #this is boolean filtering

# import numpy as np
# arr = np.array([10,20,30,40,50,60])
# print(arr[(arr>20) & (arr<60)])  #AND condition

# import numpy as mp
# arz = np.array([10,20,30,40,50,60])
# print(arz[(arz<20) | (arz>50)]) #OR condition


#Standard deviation

# import numpy as np
# A=np.array([48,49,50,51,52])
# B=np.array([10,30,50,70,90])

# print(A.std())  #Std dev shows the spread around the data center
# print(B.std())

# import numpy as np
# lis = np.array([10,20,30,40,50])
# print("Min: ",lis.min())
# print("Max: ",lis.max())
# print("Mean: ",lis.mean())
# print("Std: ",lis.std())
# print("Sorted: ",np.sort(lis))

# import numpy as np
# arr = np.array([
# [10,20,30],
# [40,50,60]
# ])
# print("Column sum: ",arr.sum(axis=0))
# print("Row sum: ",arr.sum(axis=1))
# print("Column mean: ",arr.mean(axis=0))
# print("Row mean: ",arr.mean(axis=1))
# print(arr.max(axis=0))
# print(arr.max(axis=1))

# import numpy as np
# arr = np.array([
#     [60,70,80],
#     [50,90,70],
#     [80,60,90]
# ])

# print(arr.mean(axis=0))
# print(arr.mean(axis=1))

# import numpy as np
# arr = np.array([
#     [50,60,70],
#     [80,90,100],
#     [40,50,60]
# ])
# print("Student Max: ",arr.max(axis=0))
# print("Subject Max: ",arr.max(axis=1))
# print("Student Mean: ",arr.mean(axis=0))
# print("Subject Mean: ",arr.mean(axis=1))

# import numpy as np
# marks=np.array([35,55,20,80,45,90])
# new_marks=np.where(marks<40,40,marks)
# print(new_marks)

import numpy as np
marks=np.array([
    [35,60,75],
    [80,45,90],
    [25,70,55]
])
print("Student Average: ",marks.mean(axis=1))
print("Subject Average: ",marks.mean(axis=0))
print("Highest Marks: ",marks.max())
new_marks=np.where(marks<40,40,marks)
print("Updated Marks: ",new_marks)