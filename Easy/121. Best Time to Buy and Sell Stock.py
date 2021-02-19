class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        currMin = float('inf')

        for price in prices:
            currMin = min(price, currMin)
            if price - currMin > maxProfit:
                maxProfit = price - currMin

        return maxProfit
