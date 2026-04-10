"""
Problem: Merge Sorted Array (Custom Attempt)
Platform: LeetCode

Note:
This is a custom approach using removal of zeros and appending elements.
Not the optimal solution, but written for understanding purposes.
"""

# Input
nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
nums2 = [1, 2, 2]
m = 6  # number of valid elements in nums1
n = 3  # number of elements in nums2

# Loop through a copy of nums1
for i in nums1[:]:
    # Check if m is less than total length of nums1
    if m < len(nums1):
        # If current element is 0, remove it
        if i == 0:
            nums1.remove(i)
    else:
        # Stop loop if condition fails
        break

# Loop through a copy of nums2
for j in nums2[:]:
    # Check if n is less than total length of nums2
    if n < len(nums2):
        # If element is 0, remove it from nums2
        if j == 0:
            nums2.remove(j)
    else:
        # Otherwise, append element to nums1
        nums1.append(j)

# Sort nums1 after merging
nums1.sort()

# Output result
print(nums1)
