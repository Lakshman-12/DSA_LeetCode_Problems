"""
Problem: Remove Duplicates from Sorted Array
Platform: LeetCode
Difficulty: Easy

Description:
Given a sorted array nums, remove the duplicates in-place such that each element appears only once 
and return the new length.

Do not allocate extra space for another array. You must do this by modifying the input array in-place 
with O(1) extra memory.

Example:
Input: nums = [1,1,2]
Output: 2  (nums becomes [1,2,_])

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5  (nums becomes [0,1,2,3,4,_...])

Approach (Two Pointer Technique):
- Use two pointers:
  - 'right' → tracks position of last unique element
  - 'i' → traverses the array
- If current element is different from nums[right], move 'right' forward and update value

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        right = 0  # pointer for unique elements

        for i in range(1, len(nums)):
            if nums[i] != nums[right]:
                right += 1
                nums[right] = nums[i]

        return right + 1


# # Optional: Example usage
# if __name__ == "__main__":
#     nums = [0,0,1,1,1,2,2,3,3,4]
#     sol = Solution()
#     k = sol.removeDuplicates(nums)
#     print("Unique count:", k)
#     print("Modified array:", nums[:k])
