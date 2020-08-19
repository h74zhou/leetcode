class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def feasible(cap):
            # given an input capacity "cap", return if it's possible to
            # ship all packages within D days
            currWeight, day = 0, 1
            for i in range(len(weights)):
                if currWeight + weights[i] > cap:
                    day += 1
                    currWeight = weights[i]
                elif currWeight + weights[i] == cap:
                    day += 1
                    currWeight = 0
                else:
                    currWeight += weights[i]
            return True if day <= D else False

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
