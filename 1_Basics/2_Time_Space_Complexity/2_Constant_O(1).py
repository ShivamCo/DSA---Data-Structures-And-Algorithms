# Constant Time Complexity — O(1)

# An algorithm is called Constant Time when the execution
# time remains the same regardless of input size.

# No matter how large the input becomes,
# the operation takes the same amount of time.


# Example

arr = [1, 2, 3, 4]

add = arr[1] + 10

print(add)


# -----------------------------------
# Time Complexity Analysis
# -----------------------------------

# Accessing an element using an index:
# arr[1]

# takes constant time in Python lists.

# Even if the array size increases:
# [1, 2, 3, 4]
# or
# [1, 2, 3, ..., 1000000]

# accessing arr[1] still takes the same time.

# Therefore:
# Time Complexity = O(1)


# -----------------------------------
# Space Complexity Analysis
# -----------------------------------

# The variable 'add' stores the result.

# It uses a fixed amount of memory.

# Since memory usage does not increase
# with input size:

# Space Complexity = O(1)


# -----------------------------------
# Important Note
# -----------------------------------

# In complexity analysis, constants are ignored.

# Example:
# O(4)  -> O(1)
# O(100) -> O(1)

# because they represent constant time
# or constant memory usage.