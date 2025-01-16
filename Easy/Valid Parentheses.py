"""
Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
Example 4:
Input: s = "([])"
Output: true
"""


# s = "([)]"
# s = "()"
# s = "){"
# s = "()))"
s = "[([]])"
class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) % 2 != 0:
        #     return False
        # if s[0] in (')', ']', '}'):
        #     return False
        a = []
        b = []
        for i in s:
            if i in ('(', '[', '{'):
                a.append(i)
            elif i in (')', ']', '}') and a:
                if i == ')' and '(' in a[-1]:
                    a.pop()
                elif i == ']' and '[' in a[-1]:
                    a.pop()
                elif i == '}' and '{' in a[-1]:
                    a.pop()
                # else:
                #     return False
            else:
                b.append(i)
        if a or b:
            return False
        else:
            return True

solution = Solution()

test = solution.isValid(s)
print(test)
