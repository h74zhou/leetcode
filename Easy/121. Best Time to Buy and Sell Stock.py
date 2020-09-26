class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        currMin, currMinIndex = prices[0], 0
        currMaxProfit = 0

        for i in range(1, len(prices)):
            currMin = min(currMin, prices[i])
            if prices[i] - currMin > currMaxProfit:
                currMaxProfit = prices[i] - currMin

        return currMaxProfit
