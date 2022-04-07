"""
We are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

 

Example 1:

Input: stickers = ["with","example","science"], target = "thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.
 

Constraints:

n == stickers.length
1 <= n <= 50
1 <= stickers[i].length <= 10
1 <= target.length <= 15
stickers[i] and target consist of lowercase English letters.
"""

from typing import List
import time 

class Solution:
    def isNotBetter(self, i, j, stickerStats, targetStat):
        for k in range(len(targetStat)):
            if stickerStats[i][k] > stickerStats[j][k] and stickerStats[j][k] < targetStat[k]:
                return False
        return True

    def removeUnneccessary(self, stickerStats, targetStat):
        while True:
            changed = False
            for i in range(len(stickerStats)):
                notNeed = False
                for j in range(len(stickerStats)):
                    if j == i:
                        continue
                    if self.isNotBetter(i, j, stickerStats, targetStat):
                        notNeed = True
                        del stickerStats[i]
                        break
                if notNeed:
                    changed = True
                    break
            if not changed:
                break

        return stickerStats

    def valid(self, numChosen, nStickerStats, targetStat):
        for k in range(len(targetStat)):
            s = 0
            for j in range(len(nStickerStats)):
                if nStickerStats[j][k] == 0 or numChosen[j] == 0:
                    continue
                s += numChosen[j] * nStickerStats[j][k]
            if s < targetStat[k]:
                return False
        return True

    def backtrack(self, k, idx, numChosen, nStickerStats, targetStat, mustHave):
        if idx == len(nStickerStats):
            if k > 0:
                return False
            return self.valid(numChosen, nStickerStats, targetStat)
        elif k == 0:
            return self.valid(numChosen, nStickerStats, targetStat)
        else:
            for i in range(k, 0, -1):
                numChosen[idx] = i
                if self.backtrack(k-i, idx+1, numChosen, nStickerStats, targetStat, mustHave):
                    return True

            numChosen[idx] = 0
            # if idx not in mustHave:
            if self.backtrack(k, idx+1, numChosen, nStickerStats, targetStat, mustHave):
                return True

        return False

    def minStickers(self, stickers: List[str], target: str) -> int:
        debug = False
        if debug:
            print("\n\nstart debug")
        d = {}
        for ch in target:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        keys = list(d.keys())
        targetStat = [d[key] for key in keys]
        # print(targetStat)
        if debug:
            print('len keys: ', len(keys))

        if debug:
            t1 = time.time()
        stickerStats = [[sticker.count(key) for key in keys] for sticker in stickers]
        if debug:
            t2 = time.time()
            print("stat time: ", t2 - t1)

        # remove unneccessary stickers
        if debug:
            t1 = time.time()
        # nStickerStats = [stickerStats[i] for i in range(len(stickers)) if not self.unneccessary(i, stickerStats, targetStat)]
        nStickerStats = self.removeUnneccessary(stickerStats, targetStat)
        if debug:
            t2 = time.time()
            print("unnec time: ", t2 - t1)        
            print("nStickerStats len: ", len(nStickerStats))
            print(nStickerStats)

        mustHave = [[] for i in range(len(keys))]
        for k in range(len(keys)):
            s = 0
            count = 0
            for i in range(len(nStickerStats)):
                if nStickerStats[i][k] > 0:
                    mustHave[k].append(i)
                    count += 1
                s += nStickerStats[i][k]
            if s == 0:
                return -1
            # elif count > 1:
            #     mustHave[k] = -1
        if debug:
            print(mustHave)

        for k in range (1, len(target) + 1):
            if self.backtrack(k, 0, [0 for i in range(len(nStickerStats))], nStickerStats, targetStat, mustHave):
                return k
        return -1

sol = Solution()
print(sol.minStickers(["with","example","science"], "thehat"))
print(sol.minStickers(["notice","possible"], "basicbasic"))
print(sol.minStickers(["hour","supply","plain","fruit","pretty","touch","property"],
"sharpcenter"))


print(sol.minStickers(["and","pound","force","human","fair","back","sign","course",
                        "sight","world","close","saw","best","fill","late","silent",
                        "open","noon","seat","cell","take","between","it","hundred",
                        "hat","until","either","play","triangle","stay","separate","season",
                        "tool","direct","part","student","path","ear","grow","ago",
                        "main","was","rule","element","thing","place","common","led",
                        "support","mean"]
, "quietchord"))



t1 = time.time()
print(sol.minStickers(["indicate","why","finger","star","unit","board","sister","danger",
                        "deal","bit","phrase","caught","if","other","water","huge","general",
                        "read","gold","shall","master","men","lay","party","grow","view","if",
                        "pull","together","head","thank","street","natural","pull","raise",
                        "cost","spoke","race","new","race","liquid","me","please","clear",
                        "could","reply","often","huge","old","nor"]
, "fhhfiyfdcwbycma"))
t2 = time.time()
print(t2-t1)