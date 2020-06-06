class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for j in range(len(coins)):
                if (coins[j] <= i):
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])

        return dp[amount] if dp[amount] < float('inf') else -1
