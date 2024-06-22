import numpy as np

# This is how we define a numpy array
a = np.array([1, 2, 3])
# Two-dimensional numpy array - nested lists
b = np.array([[12.0, 23.4, 7.0], [6.0, 5.0, 4.0]])

# Printing a numpy array
print(a)
print(b)

# Getting the number of dimensions of numpy array
print(a.ndim)  # a is one-dimensional numpy array
print(b.ndim)  # b is two-dimensional numpy array

# Getting the shape - refers to the number of elements in each dimension
print(b.shape)
print(f"The shape of numpy array a is {a.shape}")

# Printing the data type of the numpy arrays
print(a.dtype)
print(b.dtype)

# We can specify the data type and change it from default value.
c = np.array([1, 2, 3, 4], dtype='int32')
print(c.dtype)

# size is used for getting the total number of elements within the numpy array
print(a.size)
print(b.size)

# item size - represents the size of a single element in the NumPy array, measured in bytes.
# The default size of int64 data type in the numpy library is 8 bytes. All the integers by default have int64 data type
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

# Getting the total size of a numpy array in bytes
print(a.nbytes)
print(b.nbytes)


