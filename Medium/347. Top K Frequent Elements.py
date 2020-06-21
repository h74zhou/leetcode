import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        heap = []
        answer = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for key, value in d.iteritems():
            heapq.heappush(heap, (-value, key))

        for i in range(k):
            answer.append(heapq.heappop(heap)[1])

        return answer
