class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        currMax = 0
        dp = [[0 for x in range(len(A) + 1)] for y in range(len(B) + 1)]

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    currMax = max(dp[i][j], currMax)
                else:
                    dp[i][j] = 0

        return currMax
