import heapq


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def distance(point):
            xPoint, yPoint = point
            return sqrt((xPoint * xPoint) + (yPoint * yPoint))

        li = []
        for point in points:
            heapq.heappush(li, (distance(point), point))

        answer = []
        for i in range(K):
            answer.append(heapq.heappop(li)[1])

        return answer
