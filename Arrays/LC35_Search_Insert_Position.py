"""
Problem: Count Elements Less Than Target (Custom Approach)
Platform: LeetCode (Concept-based)

Description:
Given an array nums and an integer target, return the count of elements 
in nums that are strictly less than the target.

Example:
Input: nums = [1, 2, 3, 4], target = 3
Output: 2

Explanation:
Elements less than 3 → [1, 2]

Approach:
- Traverse the array
- Check each element
- If element is less than target, store it in a list
- Return the length of that list

Time Complexity: O(n)
Space Complexity: O(n)
"""


from typing import List


class Solution:
    def countLessThanTarget(self, nums: List[int], target: int) -> int:
        lst = []

        # Iterate through each element
        for i in nums:
            # Check if element is less than target
            if i < target:
                lst.append(i)

        # Return count of such elements
        return len(lst)


# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    target = 3

    sol = Solution()
    print(sol.countLessThanTarget(nums, target))  # Output: 2
