"""
Problem: Remove Element
Platform: LeetCode
Difficulty: Easy

Description:
Given an integer array nums and an integer val, remove all occurrences of val 
in-place and return the number of elements that are not equal to val.

The order of elements may be changed. It doesn't matter what you leave beyond the returned length.

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2  (nums becomes [2,2,...])

Approach (Two Pointer Technique):
- Use one pointer (k) to track position of valid elements
- Traverse array
- If element is not equal to val, place it at index k
- Increment k

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # pointer for valid elements

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# Alternative (Your Approach - Not Optimal)
class SolutionBrute:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums[:]:  # iterate over copy
            if i == val:
                nums.remove(i)
        return len(nums)
