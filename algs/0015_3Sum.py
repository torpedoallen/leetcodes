'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    
    def threeSum(self, nums):
        head_set = set()
        n = len(nums)
        nums.sort()
        result = []
        for idx, num in enumerate(nums):
            if num in head_set:
                continue
            if num > 0: # impossible to sum and equal 0
                break
            head_set.add(num)
            body_set = set()
            i, j = idx + 1, n - 1
            while i < j:
                if (nums[i], nums[j]) in body_set:
                    i += 1
                    j -= 1
                    continue

                sum_ = num + nums[i] + nums[j]
                if sum_ == 0:
                    body_set.add((nums[i], nums[j]))
                    result.append([num, nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif sum_ < 0:
                    i += 1
                else:
                    j -= 1
        return result

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([]))
print(Solution().threeSum([0, 0, 0]))
                    

