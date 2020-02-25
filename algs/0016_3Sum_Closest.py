'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head_set = set()
        n = len(nums)
        nums.sort()
        min_delta, result = sys.maxsize, sys.maxsize
        for idx, num in enumerate(nums):
            if num in head_set:
                continue

            head_set.add(num)
            body_set = set()
            i, j = idx + 1, n - 1
            while i < j:
                if (nums[i], nums[j]) in body_set:
                    i += 1
                    j -= 1
                    continue

                sum_ = num + nums[i] + nums[j]
                delta = sum_ - target


                if abs(delta) < min_delta:
                    min_delta = abs(delta)
                    result = sum_
                if delta == 0:
                    return sum_
                elif delta < 0:
                    i += 1
                else:
                    j -= 1
        return result

print(Solution().threeSumClosest([1, 1, 1, 0], -100))
