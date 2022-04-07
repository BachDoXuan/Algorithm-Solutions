"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.


Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        longest = 0
        for i in range(len(s)):
            c = s[i]
            if len(stk) == 0:
                stk.append([0 if c == '(' else 1, i])
            else:
                top = stk[-1]
                # print("top = ", str(top))
                if (top[0] == 0 and c == ')'):
                    del stk[-1]
                else:
                    stk.append([0 if c == '(' else 1, i])
        if len(stk) == 0:
            return len(s)
        idx = -1
        for c,i in stk:
            # print(c)
            if (i - idx - 1) > longest:
                longest = i - idx - 1
            idx = i
        if len(s) - idx - 1 > longest:
            longest = len(s) - idx - 1
        return longest

sol = Solution()
print(sol.longestValidParentheses("(()"))


        # for i in range(len(s)):
        #     stk = []
        #     valid = True
        #     for j in range(i, len(s)):
        #         c = s[j]
        #         if len(stk) > 0:
        #             top = stk[-1]
        #             if (top == '(' and c == ')'):
        #                del stk[-1]
        #             elif top == ')':
        #                 valid = False
        #                 break
        #             else:
        #                 stk.append(c)
        #         else:
        #             stk.append(c)
        #         if not valid:
        #             break
        #         if len(stk) == 0:
        #             longest = max(longest, j - i + 1)

        # return longest