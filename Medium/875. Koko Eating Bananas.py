class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def feasible(rate):
            hours = 0
            for b in piles:
                hours += b / rate
                if b % rate != 0:
                    hours += 1
            return True if hours <= H else False

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
