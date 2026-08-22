#1. Random.rand - it is used to generate decimal values from 0 to 1
# import numpy as np
# arr = np.random.rand(5)
# print(arr)

# import numpy as np
# arr = np.random.rand(2,3)
# print(arr)

#2. Randon.randint - it is used to generate integers
# import numpy as np
# arr = np.random.randint(1,100,6)
# print(arr)

# import numpy as np
# arr = np.random.randint(1,100,(3,4))  #Here we are generating a integer matrix
# print(arr)


#3. random.randn - it is used to generate random numbers that are obtained from std. normal dist.
# import numpy as np
# arr = np.random.randn(6) #it can contain negative values too
# print(arr)

#4. Random.seed - this will generate a same random sequence everytime it runs
# import numpy as np
# np.random.seed(42)  #here 42 is just a seed, if we change it to any number the random seq will change
# print(np.random.randint(1,10,5))

# import numpy as np
# arr = np.random.randint(1,50,10)
# print(arr)

# import numpy as np
# np.random.seed(2)
# print(np.random.randint(1,10,5))


#5. Broadcasting
# import numpy as np
# arr = np.array([10,20,30])
# print(arr+5)

# arc = np.array([
#     [10,20,30],
#     [40,50,60]
# ])
# print(arc+10)

# import numpy as np
# arr = np.array([
#     [10,20,30],
#     [40,50,60]
# ])
# aaa = np.array([1,2,3])
# print(arr + aaa)  #Here 2 arrays are added

# import numpy as np
# arr = np.array([10,20,30,40])
# print(np.where(arr>=30,100,arr))


#Small Project
import numpy as np
sales = np.array([
    [120,150,180,200],
    [100,130,160,190],
    [80,110,140,170]
    ])
performance = np.where(sales >= 150, "High", "Low")
product = np.where(sales.sum(axis=1) >= 600, "Excellent", "Needs Improvement")

print("Total Sales: ",sales.sum())
print("Average Sales: ",sales.mean())
print("Highest Sales: ",sales.max())
print("Lowest Sales: ",sales.min())
print("Product-wise Sales: ",sales.sum(axis=1))
print("Month-wise Sales: ",sales.sum(axis=0))
print("Performance: ")
print(performance)
print(sales[sales >= 150])
print(product)
