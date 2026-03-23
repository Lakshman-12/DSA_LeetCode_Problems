"""
Problem: Palindrome Number
Platform: LeetCode
Difficulty: Easy

Description:
Given an integer x, return True if x is a palindrome, and False otherwise.

Approach 1 (String Method):
- Convert integer to string
- Reverse string and compare

Approach 2 (Optimized - Without String):
- Reverse the number mathematically
- Compare with original number

Time Complexity:
- O(n) for string method
- O(log n) for optimized method

Space Complexity:
- O(n) for string method
- O(1) for optimized method
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Optimized Approach (recommended for interviews)
        if x < 0:
            return False

        original = x
        reverse = 0

        while x != 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return original == reverse


# Optional: Simple one-line solution (not preferred in interviews)
def isPalindrome_string(x: int) -> bool:
    return str(x) == str(x)[::-1]
