class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        totalCost = 0
        refund = []
        for costA, costB in costs:
            totalCost += costA
            refund.append(costB - costA)
        refund.sort()

        for i in range(len(costs) / 2):
            totalCost += refund[i]

        return totalCost


