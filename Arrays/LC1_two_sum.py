"""
Problem: Two Sum
Platform: LeetCode
Difficulty: Easy

Approach:
- Use a hashmap (dictionary) to store numbers and their indices.
- For each number, calculate the complement (target - number).
- If complement exists in hashmap, return indices.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
