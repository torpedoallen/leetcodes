import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
    
        if n == 1:
            return nums[0]

        v_now, v_max = 0, -sys.maxsize

        for i in range(n):
            v_now += nums[i]
            v_max = max(v_now, v_max)
            if v_now < 0:
                v_now = 0
        return v_max

