"""
Given a string s, find the length of the longest
substring
 without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        sub = ""
        for char in s:
            if char not in sub: #если символ не в подстроке, добавляем его в подстроку
                sub += char
                result = max(result, len(sub)) #ищем максимальное значение длинны подстроки и сохраняем его
            else: #если символ в подстроке
                cut = sub.index(char) #находим индекс этого символа
                sub = sub[cut+1:] + char # очищаем подстроку, до следующего символа,
                                            # который идет после дубликата и добавляем текущий символ
        return result

solution = Solution()

test = solution.lengthOfLongestSubstring("pwwkew")
print(test)