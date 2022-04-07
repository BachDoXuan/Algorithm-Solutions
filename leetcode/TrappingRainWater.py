"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution:
    def trap(self, height) -> int:
        begin = 0
        end = len(height) - 1
        trap = 0
        while begin < end:
            if height[begin] <= height[end]:
                k = begin + 1
                while k < end:
                    if height[k] <= height[begin]:
                        trap += height[begin] - height[k]
                        k += 1
                    else:
                        begin = k
                        break
                if k == end:
                    break
            else:
                k = end - 1
                while k > begin:
                    if height[k] <= height[end]:
                        trap += height[end] - height[k]
                        k -= 1
                    else:
                        end = k
                        break
                if k == begin:
                    break
        return trap

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([4,2,0,3,2,5]))