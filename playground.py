# import numpy as np

# # Python list
# a = [1, 2, 3]

# # NumPy array
# b = np.array([1, 2, 3])

# print(a * 2)   # ❌ wrong thinking
# print(b * 2)   # ✅ vectorized

# arr = np.array([10, 20, 30, 40])

# print(arr + 5)
# print(arr * 2)
# print(arr / 10)

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# print(A + B)        # element-wise
# print(A @ B)        # matrix multiplication

import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([[1, 2, 3],
#               [4, 5, 6]])

# print(a.shape)  # (3,)
# print(b.shape)  # (2,3)

# a = np.array([1, 2])
# b = np.array([[1, 2, 3],
#               [4, 5, 6]])

# print(b + a)  # ❌ ERROR

# a = np.array([1, 2])

# a = a.reshape(2, 1)

# b = np.array([[1, 2, 3],
#               [4, 5, 6]])

# print(b + a)

# data = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])




# # a=np.array([10,20,30])
# print(data+a)


# row=data+a
# b=np.array([100,200]).reshape(2,1)
# result = row+b
# print(result)

# mean = np.mean(data,axis=0)
# std=np.std(data,axis=0)
# normalization = (data-mean)/std
# print(normalization)

# print(a.shape)

import numpy as np

# a = np.array([1, 2, 3])
# # a = np.where(a == 3, 1, a)  # [1, 2, 1], shape: (3,)

# b = np.array([[1, 2, 3],
#               [3, 4, 5]])  # shape: (2, 3)


# print(a + b)
# data = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])


# a=np.array([100,200,300])
# print(data.shape)
# print(a.shape)
# print(data+a)

import numpy as np

data = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

a=np.array([100,200,300])

print(data.shape)
print(a.shape)
a=a.reshape(3,1)
print(data+a)
print(data@a)