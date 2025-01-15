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