"""
Problem: Valid Palindrome
Platform: LeetCode
Difficulty: Easy

Description:
Given a string s, return True if it is a palindrome, or False otherwise.

A palindrome is a string that reads the same forward and backward.
Ignore non-alphanumeric characters and consider only lowercase letters.

Example:
Input: "A man, a plan, a canal: Panama"
Output: True

Input: "race a car"
Output: False

Approach:
- Remove all non-alphanumeric characters
- Convert to lowercase
- Check if string is equal to its reverse

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""

        # If single character, it's always palindrome
        if len(s) == 1:
            return True

        # Filter alphanumeric characters and convert to lowercase
        for i in s:
            if i.isalnum():
                res += i.lower()

        # Check palindrome
        if res == res[::-1]:
            # Handles empty string and valid cases
            if len(res) >= 1 or res == "":
                return True
            else:
                return False
        else:
            return False


