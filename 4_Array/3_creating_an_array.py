"""
ARRAY TRAVERSAL IN PYTHON (DSA NOTES)

Traversal means visiting each element of an array exactly once.

Time Complexity:
----------------
Traversal -> O(n)
where n is the number of elements in the array.
"""

from array import *

# --------------------------------------------------
# CREATE AN ARRAY
# --------------------------------------------------

# 'i' = Signed Integer Type Code
# All elements must be integers

val = array('i', [10, 20, 30, 40, 50, 60])

print("Original Array:")
print(val)

# --------------------------------------------------
# METHOD 1: DIRECT TRAVERSAL
# --------------------------------------------------

"""
In this method, each element is accessed directly.

Advantages:
- Simple and readable
- Preferred when index is not needed

Time Complexity: O(n)
"""

print("\nTraversal Method 1 (Direct Traversal):")

for element in val:
    print(element, end=" ")

print()

# --------------------------------------------------
# METHOD 2: INDEX-BASED TRAVERSAL
# --------------------------------------------------

"""
In this method, elements are accessed using their index.

Advantages:
- Useful when index position is needed
- Common in DSA problems

Time Complexity: O(n)
"""

print("\nTraversal Method 2 (Using Index):")

for i in range(len(val)):
    print(f"Index {i} -> {val[i]}")

# --------------------------------------------------
# METHOD 3: USING ENUMERATE
# --------------------------------------------------

"""
enumerate() returns both index and value.

Time Complexity: O(n)
"""

print("\nTraversal Method 3 (Using enumerate):")

for index, value in enumerate(val):
    print(f"Index {index} -> {value}")

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

print("\nSummary:")
print("1. Direct Traversal    -> for element in array")
print("2. Index Traversal     -> for i in range(len(array))")
print("3. Enumerate Traversal -> for index, value in enumerate(array)")

"""
OUTPUT:

Original Array:
array('i', [10, 20, 30, 40, 50, 60])

Traversal Method 1 (Direct Traversal):
10 20 30 40 50 60

Traversal Method 2 (Using Index):
Index 0 -> 10
Index 1 -> 20
Index 2 -> 30
Index 3 -> 40
Index 4 -> 50
Index 5 -> 60

Traversal Method 3 (Using enumerate):
Index 0 -> 10
Index 1 -> 20
Index 2 -> 30
Index 3 -> 40
Index 4 -> 50
Index 5 -> 60
"""