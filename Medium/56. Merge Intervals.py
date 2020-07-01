class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return intervals

        def canMerge(interval1, interval2):
            front = max(interval1[0], interval2[0])
            back = min(interval1[1], interval2[1])
            return back >= front

        intervals.sort(key=lambda x: x[0])
        stack = [intervals[0]]

        for interval in intervals[1:]:
            if len(stack) == 0:
                stack.append(interval)
            else:
                if canMerge(stack[-1], interval):
                    start, end = stack.pop()
                    stack.append([min(start, interval[0]), max(end, interval[1])])
                else:
                    stack.append(interval)

        return [x for x in stack]
