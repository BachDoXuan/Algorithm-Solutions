"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dpTable = [[False for i in range(n+1)] for j in range(m+1)]
        dpTable[m][n] = True
        for c in range(m-1, -1, -1):
            pCh = p[c]
            if pCh == "*":
                continue
            if c < m-1 and p[c+1] == "*":
                # match pCh* first
                if pCh == ".":
                    idx = -1
                    for i in range(n, -1, -1):
                        # find largest idx such that dpTable[c+2][idx] is True (skip *)
                        if dpTable[c+2][i] == True:
                            idx = i
                            break
                    for i in range(idx+1, n, 1):
                        dpTable[c][i] = False
                    for i in range(idx+1):
                        dpTable[c][i] = True
                else:
                    for i in range(n, -1, -1): # boundary case n as well
                        if dpTable[c+2][i]:
                            dpTable[c][i] = True
                            continue
                        idx = i
                        while idx < n and s[idx] == pCh:
                            if dpTable[c+2][idx+1]:
                                dpTable[c][i] = True
                                break
                            idx += 1
            elif pCh == ".":
                for i in range(n-1, -1, -1):
                    dpTable[c][i] = dpTable[c+1][i+1]
            else:
                for i in range(n-1, -1, -1):
                    dpTable[c][i] = (pCh == s[i]) and dpTable[c+1][i+1]
        return dpTable[0][0]

sol = Solution()
print(not sol.isMatch("aa", "a"))
print(sol.isMatch("aa", "a*"))
print(sol.isMatch("ab", ".*"))
print(sol.isMatch("aab", "c*a*b"))
print(sol.isMatch("a", "ab*"))