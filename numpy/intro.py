import numpy as np

arr = np.array([1, 2, 3, 4, 5], dtype='int64')

print(arr)

# 8 bits = 1 byte
# arr dtype = int64
# 64 bits = 8 bytes
# arr.size = 5
# nbytes = 5 * 8 = 40 bytes

print(arr.shape, arr.size, arr.ndim, arr.dtype, arr.nbytes)


arr2 = np.array([[1, 2, 3], [11, 12, 13], [21, 22, 23]])
print(arr2)


print(arr2.shape, arr2.size, arr2.ndim, arr2.dtype, arr2.nbytes)
