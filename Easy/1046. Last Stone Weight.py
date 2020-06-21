import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        q = []

        for i in range(len(stones)):
            heapq.heappush(q, (0 - stones[i], stones[i]))

        while len(q) > 1:
            y = heapq.heappop(q)[1]
            x = heapq.heappop(q)[1]
            if x == y:
                continue
            elif x != y:
                newWeight = y - x
                heapq.heappush(q, (0 - newWeight, newWeight))

        if len(q) == 1:
            remainingStone = heapq.heappop(q)[1]
            return remainingStone
        else:
            return 0
