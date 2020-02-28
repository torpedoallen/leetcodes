class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.perms(nums)

    def perms(self, nums):
        n = len(nums)   
        if n == 0:
            return []
        if n == 1:
            return [nums]
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tmp = nums[:i] + nums[i+1:]
            for j in self.perms(tmp):
                res.append([nums[i]] + j)
        return res
            
