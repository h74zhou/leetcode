class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []

        def canMerge(interval1, interval2):
            front = max(interval1[0], interval2[0])
            back = min(interval1[1], interval2[1])
            return back >= front

        intervals.sort()
        stack, answer = [intervals[0]], []

        for i in range(1, len(intervals)):
            currInterval = intervals[i]
            prevInterval = stack.pop()
            if canMerge(prevInterval, currInterval):
                minStart = min(prevInterval[0], currInterval[0])
                maxEnd = max(prevInterval[1], currInterval[1])
                stack.append([minStart, maxEnd])
            else:
                stack.append(prevInterval)
                stack.append(currInterval)

        return stack
