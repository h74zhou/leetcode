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
            return 0 - sqrt((xPoint * xPoint) + (yPoint * yPoint))

        li = []
        for point in points:
            if len(li) < K:
                heapq.heappush(li, (distance(point), point))
            elif distance(point) < li[0]:
                heapq.heappushpop(li, (distance(point), point))

        answer = []
        for point in li:
            answer.append(point[1])

        return answer
