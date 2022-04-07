"""
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums[i] * nums[j] is divisible by k.
 

Example 1:

Input: nums = [1,2,3,4,5], k = 2
Output: 7
Explanation: 
The 7 pairs of indices whose corresponding products are divisible by 2 are
(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), and (3, 4).
Their products are 2, 4, 6, 8, 10, 12, and 20 respectively.
Other pairs such as (0, 2) and (2, 4) have products 3 and 15 respectively, which are not divisible by 2.    
Example 2:

Input: nums = [1,2,3,4], k = 5
Output: 0
Explanation: There does not exist any pair of indices whose corresponding product is divisible by 5.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 105
"""
from typing import List
from math import gcd, lcd


class Solution:
    def gcd(self, n: int, m: int) -> int:
        x1 = n if n <= m else m
        x2 = m if n <= m else n
        while x1 > 0:
            tmp = x2 % x1
            x2 = x1
            x1 = tmp
        return x2
    # def gcd(self, a, b):
    
    #     # GCD(0, b) == b; GCD(a, 0) == a,
    #     # GCD(0, 0) == 0
    #     if (a == 0):
    #         return b
    
    #     if (b == 0):
    #         return a
    
    #     # Finding K, where K is the
    #     # greatest power of 2 that
    #     # divides both a and b.
    #     k = 0
    
    #     while(((a | b) & 1) == 0):
    #         a = a >> 1
    #         b = b >> 1
    #         k = k + 1
    
    #     # Dividing a by 2 until a becomes odd
    #     while ((a & 1) == 0):
    #         a = a >> 1
    
    #     # From here on, 'a' is always odd.
    #     while(b != 0):
    
    #         # If b is even, remove all
    #         # factor of 2 in b
    #         while ((b & 1) == 0):
    #             b = b >> 1
    
    #         # Now a and b are both odd. Swap if
    #         # necessary so a <= b, then set
    #         # b = b - a (which is even).
    #         if (a > b):
    
    #             # Swap u and v.
    #             temp = a
    #             a = b
    #             b = temp
    
    #         b = (b - a)
    
    #     # restore common factors of 2
    #     return (a << k)

    def countPairs(self, nums: List[int], k: int) -> int:
        counts = [0 for i in range(k+ 1)]
        for i in range(1, k):
            if k % i == 0:
                for num in nums:
                    if num % i == 0:
                        counts[i] += 1
        for num in nums:
            if num % k == 0:
                counts[k] += 1
        
        numPairs = 0
        for num in nums:
            d = self.gcd(num, k)
            q = k // d
            numPairs += counts[q]
            if num % q == 0:
                numPairs -= 1
        return numPairs // 2


sol = Solution()

print(sol.countPairs([1,2,3,4,5], 2))
print(sol.countPairs([1,2,3,4], 5))