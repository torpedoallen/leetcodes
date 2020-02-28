class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        i, j = 0, 0
        if n == 0:
            return 0

        while i < m:
            if haystack[i] == needle[j]:
                j += 1
                if j == n:
                    return i - j + 1
            else:
                i = i - j
                j = 0
            i += 1
        return -1
