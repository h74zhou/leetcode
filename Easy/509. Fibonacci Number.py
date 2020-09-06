class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1

        dp = []
        dp.append(0)
        dp.append(1)

        for i in range(2, N + 1):
            dp.append(dp[i - 2] + dp[i - 1])

        return dp[-1]
