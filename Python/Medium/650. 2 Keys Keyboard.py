class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        dp = [float('inf')] * (n + 1)
        dp[1] = 0

        for k in range(2, n + 1):
            for i in range(1, k):
                if k % i != 0:
                    continue
                dp[k] = min(dp[k], dp[i] + k / i)

        return dp[-1]
