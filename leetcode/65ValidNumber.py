"""
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

 

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""

class Solution:
    def isDecimal(self, s: str) -> bool:
        idx = 0
        if s[idx] == "+" or s[idx] == "-":
            idx += 1
            if len(s) == 1:
                return False
        hasDigitBeforeDot = False
    
        while idx < len(s):
            if s[idx] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                idx += 1
                hasDigitBeforeDot = True
            else:
                break
    
        if idx == len(s):
            return True
        elif s[idx] != ".":
            return False
        idx += 1
        if idx == len(s) and not hasDigitBeforeDot:
            return False

        while idx < len(s):
            if s[idx] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                idx += 1
            else:
                return False
        return True


    def isInteger(self, s: str) -> bool:
        idx = 0
        if s[idx] == "+" or s[idx] == "-":
            idx += 1
            if len(s) == 1:
                return False
        while idx < len(s):
            if s[idx] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                idx += 1
            else:
                return False
        return True

    def isNumber(self, s: str) -> bool:
        eIdx = s.find("e")
        if eIdx == len(s) - 1 or eIdx == 0:
            return False
        elif eIdx > 0:
            return (self.isDecimal(s[:eIdx]) or self.isInteger(s[:eIdx])) and self.isInteger(s[eIdx+1:])
        else:
            EIdx = s.find("E")
            if EIdx == len(s) - 1 or EIdx == 0:
                return False
            elif EIdx > 0:
                return (self.isDecimal(s[:EIdx]) or self.isInteger(s[:EIdx])) and self.isInteger(s[EIdx+1:])
            else:
                return (self.isDecimal(s) or self.isInteger(s))

sol = Solution()
print(sol.isNumber("0"))
print(sol.isNumber("e"))
print(sol.isNumber("."))

print("Follows are true: ")
for s in ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]:
    print(sol.isNumber(s))

print("Follows are false:")
for s in ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]:
    print(sol.isNumber(s))