"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109

"""

from typing import List

class Solution:
    def bucketSort(self, nums: List[int], exp: int):
        buckets = [[] for i in range(10)]
        for num in nums:
            buckets[(num // exp) % 10].append(num)
        nums = []
        for i in range(len(buckets)):
            for num in buckets[i]:
                nums.append(num)
        return nums

    def radixSort(self, nums: List[int]):
        maxNum = max(nums)
        exp = 1
        while (maxNum / exp) > 0:
            nums = self.bucketSort(nums, exp)
            exp *= 10

        return nums

    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums = self.radixSort(nums)
        maxGap = -1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > maxGap:
                maxGap = diff
        return maxGap

sol = Solution()

print(sol.maximumGap([3,6,9,1]))
print(sol.maximumGap([10]))
print(sol.maximumGap([100,3,2,1]))