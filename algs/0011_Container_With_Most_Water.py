'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''





class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_v = -1
        i, j, max_v = 0, n - 1, -1
        while i < j:
            if height[i] < height[j]:
                max_v = max(max_v, (j - i)*height[i])
                i += 1
            else:
                max_v = max(max_v, (j - i)*height[j])
                j -= 1
        return max_v
