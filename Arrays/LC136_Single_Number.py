"""
Problem: Find Element with Frequency One (Single Number Variant)
Platform: LeetCode (Concept-based)

Description:
Given an array of integers, find and return the element that appears only once.
All other elements appear more than once.

Example:
Input: nums = [2, 2, 1]
Output: 1

Approach:
- Use a dictionary to count frequency of each element
- Traverse dictionary to find element with frequency = 1
- Return that element

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}

        # Count frequency of each element
        for i in nums:
            if str(i) not in d:
                d[str(i)] = 1
            else:
                d[str(i)] += 1

        # Find element with frequency 1
        for j in d:
            if d[j] == 1:
                return int(j)


# Example usage
if __name__ == "__main__":
    nums = [2, 2, 1]
    sol = Solution()
    print(sol.singleNumber(nums))  # Output: 1
