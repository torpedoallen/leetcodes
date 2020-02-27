class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return nums
        if n == 1:
            return [nums]
        res = []
        for i in range(n):
            tmp = nums[:i] + nums[i+1:]
            for j in self.permute(tmp):
                res.append([nums[i]]+j)
        return res
