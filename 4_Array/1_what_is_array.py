"""
ARRAYS IN PYTHON (DSA BASICS)

An array is a collection of elements stored in sequential order.
In Python, we typically use a LIST as an array.

Example:
Index:  0   1   2   3   4
Array: [10, 20, 30, 40, 50]

Accessing an element by index is O(1).
"""

# ---------------------------
# 1. Creating an Array
# ---------------------------

arr = [10, 20, 30, 40, 50]
print("Original Array:", arr)

# Empty array
empty_arr = []
print("Empty Array:", empty_arr)

# Array with fixed size (5 zeros)
fixed_arr = [0] * 5
print("Fixed Size Array:", fixed_arr)

print("\n" + "=" * 40)

# ---------------------------
# 2. Accessing Elements
# ---------------------------

print("First Element:", arr[0])
print("Third Element:", arr[2])

print("\n" + "=" * 40)

# ---------------------------
# 3. Updating Elements
# ---------------------------

arr[1] = 99
print("After Updating Index 1:", arr)

print("\n" + "=" * 40)

# ---------------------------
# 4. Traversing an Array
# ---------------------------

print("Traversing Using Index:")

for i in range(len(arr)):
    print(f"Index {i}: {arr[i]}")

print("\nTraversing Directly:")

for value in arr:
    print(value)

print("\n" + "=" * 40)

# ---------------------------
# 5. Insert Operations
# ---------------------------

# Insert at end
arr.append(60)
print("After append(60):", arr)

# Insert at specific index
arr.insert(2, 25)
print("After insert(2, 25):", arr)

print("\n" + "=" * 40)

# ---------------------------
# 6. Delete Operations
# ---------------------------

# Remove by value
arr.remove(25)
print("After remove(25):", arr)

# Remove by index
removed = arr.pop(3)
print("Removed Element:", removed)
print("After pop(3):", arr)

print("\n" + "=" * 40)

# ---------------------------
# 7. Searching (Linear Search)
# ---------------------------

target = 40
found = False

for i in range(len(arr)):
    if arr[i] == target:
        print(f"{target} found at index {i}")
        found = True
        break

if not found:
    print(f"{target} not found")

print("\n" + "=" * 40)

# ---------------------------
# 8. Time Complexities
# ---------------------------

print("Time Complexities:")
print("Access by Index      -> O(1)")
print("Update by Index      -> O(1)")
print("Search               -> O(n)")
print("Insert at End        -> O(1) amortized")
print("Insert in Middle     -> O(n)")
print("Delete in Middle     -> O(n)")

print("\n" + "=" * 40)

# ---------------------------
# 9. Complete Example
# ---------------------------

numbers = [5, 10, 15, 20]

print("Initial:", numbers)

# Access
print("First Element:", numbers[0])

# Update
numbers[2] = 99

# Insert
numbers.append(25)

# Traverse
print("Final Array:")

for num in numbers:
    print(num)

"""
OUTPUT (approximately)

Original Array: [10, 20, 30, 40, 50]
Empty Array: []
Fixed Size Array: [0, 0, 0, 0, 0]

========================================
First Element: 10
Third Element: 30

========================================
After Updating Index 1: [10, 99, 30, 40, 50]

...
"""