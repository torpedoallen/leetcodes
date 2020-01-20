

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        revs = dict([(num, n) for n, num in enumerate(nums)])
        for n, num in enumerate(nums):
            diff = target - num
            if diff in revs and revs[diff] != n:
                return n, revs[diff]




if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 3], 6))


            
