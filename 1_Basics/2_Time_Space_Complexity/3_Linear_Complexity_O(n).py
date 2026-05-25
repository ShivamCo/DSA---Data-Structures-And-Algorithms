# Linear Time and Space Complexity — O(n)

# In Linear Complexity, the time or space used
# grows linearly with the input size (n).

# If the input size increases,
# the complexity also increases proportionally.


# -----------------------------------
# Linear Time Complexity
# -----------------------------------

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop runs once for every element in the array
for i in arr1:
    print(i)


# Time Complexity Analysis

# If the array contains:
# 10 elements -> loop runs 10 times
# 100 elements -> loop runs 100 times
# n elements -> loop runs n times

# Therefore:
# Time Complexity = O(n)

# Here:
# Array creation -> O(1)
# Loop execution -> O(n)

# Total:
# O(1) + O(n)

# We ignore constants in complexity analysis,
# so final complexity becomes:

# O(n)


# -----------------------------------
# Linear Space Complexity
# -----------------------------------

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr3 = []

# Loop runs for every element in arr2
for i in arr2:
    arr3.append(i)


# Space Complexity Analysis

# arr3 stores all elements from arr2.

# If arr2 has:
# 10 elements -> arr3 stores 10 elements
# 100 elements -> arr3 stores 100 elements
# n elements -> arr3 stores n elements

# Extra space grows with input size.

# Therefore:
# Space Complexity = O(n)

# Here:
# arr2 -> O(1)
# arr3 initialization -> O(1)
# Additional stored elements -> O(n)

# Total:
# O(1) + O(1) + O(n)

# Final Complexity:
# O(n)