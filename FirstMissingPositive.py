"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)): 
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 0
                continue
            if nums[i] == i+1:
                continue
            tmp = nums[nums[i]-1]
            nums[nums[i]-1] = nums[i]
            k = nums[i]-1
            while True:
                if tmp > len(nums) or tmp <= 0 or tmp == k+1:
                    break
                tmp2 = nums[tmp-1]
                nums[tmp-1] = tmp
                k = tmp-1
                tmp = tmp2
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1

sol = Solution()
print(sol.firstMissingPositive([1,2,0]))
print(sol.firstMissingPositive([3,4,-1,1]))
print(sol.firstMissingPositive([7,8,9,11,12]))