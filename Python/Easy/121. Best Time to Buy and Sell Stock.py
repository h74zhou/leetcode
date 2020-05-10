class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        min = prices[0]
        max = 0

        for i in range(1, len(prices)):
            cost = prices[i]
            if cost < min:
                min = cost
            elif cost - min > max:
                max = cost - min

        return max
