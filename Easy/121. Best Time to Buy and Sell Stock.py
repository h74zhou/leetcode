class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        maxProfit = 0
        currMin = prices[0]
        for i in range(len(prices)):
            if prices[i] - currMin > maxProfit:
                maxProfit = prices[i] - currMin
            elif prices[i] < currMin:
                currMin = prices[i]

        return maxProfit
