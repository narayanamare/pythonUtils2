# Problem Statement
# Given an array arr of size n, rotate its elements to the right by k places.

# arr = [1, 2, 3, 4, 5], k = 2
# Rotated array → [4, 5, 1, 2, 3]

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    if k == 0:
        return arr
    # Brute-force rotation using slicing
    return arr[-k:] + arr[:-k]

# Example
arr = [1, 2, 3, 4, 5]
k = 2
rotated = rotate_array(arr, k)
print(rotated)  # Output: [4, 5, 1, 2, 3]
