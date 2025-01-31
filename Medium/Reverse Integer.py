"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
Example 2:
Input: x = -123
Output: -321
Example 3:
Input: x = 120
Output: 21
"""
#решение номер 1
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negativ = -1
            x = str(abs(x))
            x = x[::-1]
            x = int("".join(x)) * negativ
            if x in range(-2 ** 31, 2 ** 31):
                return x
            else:
                return 0
        else:
            x = str(abs(x))
            x = x[::-1]
            x = int("".join(x))
            if x in range(-2 ** 31, 2 ** 31):
                return x
            else:
                return 0


#решение номер 2
class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
        if reversed_num in range(-2**31, 2**31):
            return reversed_num
        else:
            return 0