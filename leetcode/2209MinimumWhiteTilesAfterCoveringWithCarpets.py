"""
You are given a 0-indexed binary string floor, which represents the colors of tiles on a floor:

floor[i] = '0' denotes that the ith tile of the floor is colored black.
On the other hand, floor[i] = '1' denotes that the ith tile of the floor is colored white.
You are also given numCarpets and carpetLen. You have numCarpets black carpets, each of length carpetLen tiles. Cover the tiles with the given carpets such that the number of white tiles still visible is minimum. Carpets may overlap one another.

Return the minimum number of white tiles still visible.

Example 1:

Input: floor = "10110101", numCarpets = 2, carpetLen = 2
Output: 2
Explanation: 
The figure above shows one way of covering the tiles with the carpets such that only 2 white tiles are visible.
No other way of covering the tiles with the carpets can leave less than 2 white tiles visible.
Example 2:

Input: floor = "11111", numCarpets = 2, carpetLen = 3
Output: 0
Explanation: 
The figure above shows one way of covering the tiles with the carpets such that no white tiles are visible.
Note that the carpets are able to overlap one another.

Constraints:

1 <= carpetLen <= floor.length <= 1000
floor[i] is either '0' or '1'.
1 <= numCarpets <= 1000
"""


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        # dpTable = [[0 for i in range(len(floor))] for j in range(numCarpets + 1)]
        # numWhites = 0
        # for i in range(len(floor)):
        #     if floor[i] == '1':
        #         numWhites += 1
        # # print(numWhites)
        # # for i in range(len(floor)):
        # #     dpTable[0][i] = numWhites

        # for r in range(1, numCarpets + 1):
        #     numWhitesCovered = 0
        #     for i in range(carpetLen):
        #         if floor[i] == '1': numWhitesCovered += 1
        #         dpTable[r][i] = numWhitesCovered
        #     # for i in range(carpetLen):
        #     #     dpTable[r][i] = numWhites - numWhitesCovered
        #     for i in range(carpetLen, len(floor)):
        #         if floor[i] == '1': numWhitesCovered += 1
        #         if floor[i-carpetLen] == '1': numWhitesCovered -= 1
        #         dpTable[r][i] = max(numWhitesCovered + dpTable[r-1][i-carpetLen], dpTable[r][i-1])

        
        # return numWhites - dpTable[numCarpets][len(floor)-1]
        old = [0 for i in range(len(floor))]
        current = [0 for i in range(len(floor))]
        numWhites = 0
        for i in range(len(floor)):
            if floor[i] == '1':
                numWhites += 1

        for r in range(1, numCarpets + 1):
            numWhitesCovered = 0
            for i in range(carpetLen):
                if floor[i] == '1': numWhitesCovered += 1
                current[i] = numWhitesCovered

            for i in range(carpetLen, len(floor)):
                if floor[i] == '1': numWhitesCovered += 1
                if floor[i-carpetLen] == '1': numWhitesCovered -= 1
                current[i] = max(numWhitesCovered + old[i-carpetLen], current[i-1])
            tmp = old
            old = current
            current = tmp

        
        return numWhites - old[len(floor)-1]

sol = Solution()
print(sol.minimumWhiteTiles("10110101", 2, 2))
print(sol.minimumWhiteTiles("11111", 2, 3))