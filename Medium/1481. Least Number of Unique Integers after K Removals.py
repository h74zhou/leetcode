import heapq

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        for num in arr:
            d[num] = d.get(num, 0) + 1

        l = []
        for num, count in d.iteritems():
            heapq.heappush(l, (count, num))

        for i in range(k):
            newTuple = (l[0][0] - 1, l[0][1])
            if newTuple[0] < 1:
                heapq.heappop(l)
            else:
                l[0] = newTuple

        return len(l)

