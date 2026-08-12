# import numpy as np
# arr = np.array([5,10,15])
# print(arr*3)

# import numpy as np
# ark = np.array([
#     [1,2],
#     [3,4]
# ])
# print(ark.shape)

# import numpy as zain
# aaa = zain.array([10,20,30,40,50])
# print(aaa)

# import numpy as zain
# arr = zain.array([
#     [1,2],
#     [3,4],
#     [5,6]
# ])
# print(arr.shape)

# import numpy as np
# arr = np.array([
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ])
# print(arr[1:,1:])

# import numpy as np
# arr = np.array([
#     [10,20],
#     [30,40],
#     [50,60]
# ])
# print("Array: ", arr)
# print("Shape: ", arr.shape)
# print("Multiply by 2: ", arr * 2)

import numpy as np
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(arr[:,2])
print(arr[0:2, 1:]) # 0:2 is calling 2 rows(r0 & r1)
print(arr[1:, 0:2]) # here 1: means row1 & row2