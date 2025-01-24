"""
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Расширение для нечетных палиндромов (один центр)
            odd_palindrome = expandAroundCenter(i, i)
            # Расширение для четных палиндромов (два центра)
            even_palindrome = expandAroundCenter(i, i + 1)
            # Выбираем самый длинный
            longest = max(longest, odd_palindrome, even_palindrome, key=len)

        return longest

solution = Solution()
s = "aс"
print(solution.longestPalindrome(s))
