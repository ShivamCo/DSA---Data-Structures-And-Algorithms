"""
ARRAYS IN PYTHON (DSA NOTES)

Python provides an 'array' module for storing elements of the same data type.
Arrays are memory-efficient compared to lists.

Time Complexities:
--------------------------------
Access            -> O(1)
Update            -> O(1)
Traversal         -> O(n)
Search            -> O(n)
Append            -> O(1)
Insert at Index   -> O(n)
Delete            -> O(n)
--------------------------------
"""

from array import *

# --------------------------------------------------
# CREATE AN ARRAY
# --------------------------------------------------

arr = array('i', [10, 20, 30, 40, 50, 60])

print("Original Array:")
for i in arr:
    print(i, end=" ")
print("\n")

# Type of array
print("Type Code:", arr.typecode)

# --------------------------------------------------
# INSERTION
# --------------------------------------------------

# Insert 100 at index 2
arr.insert(2, 100)

# Insert at end
arr.append(32)

print("\nAfter Insertions:")
for i in arr:
    print(i, end=" ")
print("\n")

# --------------------------------------------------
# UPDATE
# --------------------------------------------------

# Replace element at index 3
arr[3] = 112

print("After Updating Index 3:")
for i in arr:
    print(i, end=" ")
print("\n")

# --------------------------------------------------
# ACCESSING ELEMENTS
# --------------------------------------------------

print("Element at Index 0:", arr[0])
print("Element at Index 2:", arr[2])

# --------------------------------------------------
# TRAVERSAL
# --------------------------------------------------

print("\nTraversing Array:")

for element in arr:
    print(element, end=" ")
print("\n")

# --------------------------------------------------
# SEARCHING (LINEAR SEARCH)
# --------------------------------------------------

target = 50
found = False

for i in range(len(arr)):
    if arr[i] == target:
        print(f"{target} found at index {i}")
        found = True
        break

if not found:
    print(f"{target} not found")

# --------------------------------------------------
# COPYING ARRAYS
# --------------------------------------------------

"""
1. Shallow Copy
   b = a
   Both variables point to the same object.

2. Deep Copy
   Creates a separate array in memory.
"""

copyArray = array(arr.typecode, arr)

print("\nOriginal Array:", arr)
print("Copied Array  :", copyArray)

copyArray[0] = 10001

print("\nAfter Modifying Copied Array:")
print("Original Array:", arr)
print("Copied Array  :", copyArray)

# --------------------------------------------------
# DELETION
# --------------------------------------------------

arr.pop()      # Remove last element
arr.pop(2)     # Remove element at index 2

print("\nAfter pop operations:")
print(arr)

# Remove a specific value
arr.remove(10)

print("After removing value 10:")
print(arr)

# --------------------------------------------------
# SLICING
# --------------------------------------------------

arr_1 = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Slice from index 2 to end
slice_1 = arr_1[2:]

# Reverse using slicing
reverse_arr = arr_1[::-1]

print("\nOriginal Array:", arr_1)
print("Slice [2:]     :", slice_1)
print("Reversed Array :", reverse_arr)

# --------------------------------------------------
# USER INPUT ARRAY
# --------------------------------------------------

input_arr = array('i', [])

n = int(input("\nHow many elements do you want in the array? "))

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    input_arr.append(num)

print("\nUser Array:")
for i in input_arr:
    print(i, end=" ")

print("\n")

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

print("DSA Array Operations Completed Successfully!")