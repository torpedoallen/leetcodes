class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1) + 1
        n = len(text2) + 1
        A = text1
        B = text2
        dp = [[0 for _ in range(n)]for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
