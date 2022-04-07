"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        # Handle n = 0 or m = 0 first
        if n == 0:
            for ch in p:
                if ch != "*":
                    return False
            return True
        elif m == 0:
            return False

        dpTable = [[False for i in range(n+1)] for j in range(m+1)]
        dpTable[m][n] = True

        dpMaxColMatchIndice = [n for i in range(m+1)]
        for r in range(m-1, -1, -1):
            pCh = p[r]
            if pCh == '*':
                for i in range(dpMaxColMatchIndice[r+1]+1, n, 1):
                    dpTable[r][i] = False
                if dpMaxColMatchIndice[r+1] >= 0:
                    for i in range(dpMaxColMatchIndice[r+1]+1):
                        dpTable[r][i] = True
                dpMaxColMatchIndice[r] = dpMaxColMatchIndice[r+1]
            elif pCh == "?":
                for i in range(n-1, -1, -1):
                    dpTable[r][i] = dpTable[r+1][i+1]
                dpMaxColMatchIndice[r] = dpMaxColMatchIndice[r+1] - 1
            else:
                dpMaxColMatchIndice[r] = -1
                for i in range(n-1, -1, -1):
                    if pCh == s[i] and dpTable[r+1][i+1]:
                        dpTable[r][i] = True
                        if dpMaxColMatchIndice[r] == -1:
                            dpMaxColMatchIndice[r] = i

        return dpTable[0][0]


sol = Solution()

print(sol.isMatch("aa", "a"))
print(sol.isMatch("aa", "*"))
print(sol.isMatch("cb", "?a"))