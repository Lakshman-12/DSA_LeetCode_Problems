"""
Problem: Longest Common Prefix
Platform: LeetCode
Difficulty: Easy

Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example:
Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""

Approach 1 (Shortest String Comparison):
- Find the shortest string
- Compare each character with all strings
- Stop when mismatch occurs

Time Complexity: O(n * m)
n = number of strings
m = length of shortest string

Space Complexity: O(1)
"""


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        smallest = min(strs, key=len)
        result = ""

        for i in range(len(smallest)):
            for word in strs:
                if word[i] != smallest[i]:
                    return result
            result += smallest[i]

        return result



        return prefix
