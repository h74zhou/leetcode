import heapq


class Solution(object):
    def minMeetingRooms(self, meetings):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        arr = [meetings[0][1]]

        for i in range(1, len(meetings)):
            start, end = meetings[i][0], meetings[i][1]
            lastEnd = heapq.heappop(arr)
            if start <= lastEnd:
                heapq.heappush(arr, end)
            else:
                lastEnd = end
            heapq.heappush(arr, lastEnd)

        return len(arr)


sol = Solution()
print sol.minMeetingRooms([[7, 10], [2, 4]])
