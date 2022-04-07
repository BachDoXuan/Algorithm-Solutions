"""
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
 

Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        k = len(words[0])
        if len(s) < len(words) * k: return []
        res = []

        for i in range(len(s) - len(words) * k + 1):
            tmpD = d.copy()
            isMatch = True
            for j in range(len(words)):
                w = s[(i + j * k) : (i + (j+1) * k)]
                if (not (w in tmpD)) or (tmpD[w] == 0):
                    isMatch = False
                    break
                else:
                    tmpD[w] -= 1
            if isMatch:
                res.append(i)
        return res
            

