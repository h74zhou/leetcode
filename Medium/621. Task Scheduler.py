class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = {}
        mode = 0
        for task in tasks:
            if task in d:
                d[task] += 1
            else:
                d[task] = 1
            mode = max(mode, d[task])

        count = (mode - 1) * (n + 1)
        for index, value in d.iteritems():
            if value == mode:
                count += 1

        return max(count, len(tasks))
