"""
Problem: Happy Number
Platform: LeetCode
Difficulty: Easy

Description:
Write an algorithm to determine if a number n is a happy number.

A happy number is defined by the following process:
- Replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (happy) 
  or it loops endlessly in a cycle (not happy).

Return True if n is a happy number, otherwise False.

Example:
Input: n = 19
Output: True

Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1 → Happy Number

Approach (Custom Logic):
- Repeatedly compute sum of squares of digits
- Stop when number becomes 1
- Otherwise, return False

Time Complexity: O(log n)
Space Complexity: O(1)
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        val1 = 0
        val = 0

        # Continue until number becomes single digit or equals 7
        while len(str(n)) > 1 or n == 7:
            for i in str(n):
                val += int(i) ** 2

            n = val
            val = val1  # reset value

        if n == 1:
            return True
        else:
            return False


