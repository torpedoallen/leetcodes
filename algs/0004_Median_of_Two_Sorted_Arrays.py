













'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

import sys


class Solution:

    def next_val(self, arr, idx):
        n = len(arr)
        if idx > n - 1:
            return sys.maxsize
        else:
            return arr[idx]


    def findMedianSortedArrays(self, nums1, nums2):
        # nums1 取i个元素, nums2取j个元素拼成新的数组A，nums1与nums2剩下的元素组成数组B
        # 其中len(A) == len(B) (偶数), 或len(A) = len(B) - 1 (奇数)
        # (max(A) + min(B)) / 2 或 min(B)
        n1 = len(nums1)
        n2 = len(nums2)
        target = (n1 + n2) // 2
        prev, curr = -sys.maxsize, -sys.maxsize
        idx1, idx2 = 0, 0
        while target > 0:
            n1_v = self.next_val(nums1, idx1)
            n2_v = self.next_val(nums2, idx2)
            if n2_v <= n1_v:
                prev, curr = curr, n2_v
                idx2 += 1
            else:
                prev, curr = curr, n1_v
                idx1 += 1
            target -= 1
        next_v = min(self.next_val(nums1, idx1), self.next_val(nums2, idx2))
        if (n1 + n2) % 2:
            return next_v/1.0
        else:
            return (curr + next_v)/2.0

print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
print(Solution().findMedianSortedArrays([1, 3], [2]))
print(Solution().findMedianSortedArrays([0, 0], [0]))
print(Solution().findMedianSortedArrays([0, 0], [0, 0]))
print(Solution().findMedianSortedArrays([0, 0], []))
            
            

