# Logarithmic Time Complexity — O(log n)

# Binary Search is an example of Logarithmic Time Complexity.

# In every iteration, the search space is divided into half.

# Because of this, the number of operations grows very slowly
# even when the input size becomes very large.


# -----------------------------------
# Example: Binary Search
# -----------------------------------

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

target = 70

start = 0
end = len(arr) - 1


while start <= end:

    # Find middle index
    mid = (start + end) // 2

    # Check if target is found
    if arr[mid] == target:
        print(f"Target {target} found at index {mid}")
        break

    # If target is smaller,
    # search in left half
    elif arr[mid] > target:
        end = mid - 1

    # If target is greater,
    # search in right half
    else:
        start = mid + 1


# -----------------------------------
# Time Complexity Analysis
# -----------------------------------

# Binary Search divides the array into half
# during every iteration.

# Example:
# 1000 elements
# -> 500
# -> 250
# -> 125
# -> ...

# Because the search space keeps shrinking by half:

# Time Complexity = O(log n)


# -----------------------------------
# Space Complexity Analysis
# -----------------------------------

# We only use a few variables:
# start
# end
# mid
# target

# No extra array or data structure is created.

# Therefore:
# Space Complexity = O(1)


# -----------------------------------
# Important Note
# -----------------------------------

# Binary Search only works on:
# Sorted Arrays / Sorted Lists