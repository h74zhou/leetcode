class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        side = len(A)
        dp = [[0 for x in range(side)] for y in range(side)]

        for i in range(len(A)):
            for j in range(len(A)):
                if i == 0:
                    dp[i][j] = A[i][j]
                else:
                    left = dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else float('inf')
                    top = dp[i - 1][j] if i - 1 >= 0 else float('inf')
                    right = dp[i - 1][j + 1] if i - 1 >= 0 and j + 1 < len(A) else float('inf')
                    dp[i][j] = min(left, top, right) + A[i][j]

        return min(dp[-1])
