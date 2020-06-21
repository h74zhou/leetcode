class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []  # list of perfect squares
        for i in range(1, n + 1):
            if i * i <= n:
                squares.append(i * i)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for square in squares:
            for i in range(square, n + 1):
                dp[i] = min(dp[i], 1 + dp[i - square])

        return dp[n] if dp[n] != float('inf') else 0
