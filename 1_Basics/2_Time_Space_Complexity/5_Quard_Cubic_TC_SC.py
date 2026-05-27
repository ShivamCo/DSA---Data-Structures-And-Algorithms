# Quadratic Time Complexity — O(n²)

# Quadratic Complexity happens when
# we use nested loops.

# For every element, the loop runs again
# through all elements.

# As input size increases,
# operations increase very quickly.


# -----------------------------------
# Example: Find Pairs Whose Sum is 10
# -----------------------------------

arr = [1, 0, 4, 6, 7, 9]

target = 10


for i in arr:          # Runs n times
    for j in arr:      # Runs n times again

        if i + j == target:
            print(f"First: {i}, Second: {j}")


# -----------------------------------
# Time Complexity Analysis
# -----------------------------------

# Outer loop  -> O(n)
# Inner loop  -> O(n)

# Total Complexity:
# O(n) * O(n)

# Final Time Complexity:
# O(n²)


# -----------------------------------
# Space Complexity Analysis
# -----------------------------------

# We are only using:
# i
# j
# target

# No extra array or large data structure is created.

# Therefore:
# Space Complexity = O(1)


# -----------------------------------
# Important Note
# -----------------------------------

# Nested loops usually lead to:
# O(n²)

# Three nested loops usually lead to:
# O(n³)


# Example of Cubic Complexity — O(n³)

for i in arr:
    for j in arr:
        for k in arr:
            print(i, j, k)


# Time Complexity:
# O(n³)