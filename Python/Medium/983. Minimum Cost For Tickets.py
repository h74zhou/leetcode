class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        travel = [False] * (days[-1] + 1)
        dp = [0] * (days[-1] + 1)
        for i in days:
            travel[i] = True

        for i in range(1, days[-1] + 1):
            if travel[i] == False:
                dp[i] = dp[i - 1]
            else:
                one = dp[max(i - 1, 0)] + costs[0]
                seven = dp[max(i - 7, 0)] + costs[1]
                thirty = dp[max(i - 30, 0)] + costs[2]
                dp[i] = min(one, seven, thirty)

        return dp[-1]
