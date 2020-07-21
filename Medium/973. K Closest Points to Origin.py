import heapq


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def distance(point):
            y = abs(point[1] - 0)
            x = abs(point[0] - 0)
            return 0 - sqrt((y * y) + (x * x))

        arr = []
        for point in points:
            if len(arr) < K:
                heapq.heappush(arr, (distance(point), point))
            elif distance(point) > arr[0][0]:
                heapq.heappop(arr)
                heapq.heappush(arr, (distance(point), point))

        return [x[1] for x in arr]
