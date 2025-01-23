"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # Для 0 или 1 результат равен самому числу

        left, right = 1, x // 2  # Достаточно искать до x//2 для x > 1

        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid

            if mid_squared == x:
                return mid  # Найден точный квадратный корень
            elif mid_squared < x:
                left = mid + 1  # Ищем в правой половине
            else:
                right = mid - 1  # Ищем в левой половине

        return right  # Возвращаем правую границу — это искомый корень

solution = Solution()
test = solution.mySqrt(8)
print(test)