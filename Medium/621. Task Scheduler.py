class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        freq = 0
        d = {}

        for task in tasks:
            if task in d:
                d[task] += 1
            else:
                d[task] = 1
            freq = max(freq, d[task])

        count = (n + 1) * (freq - 1)

        for index, value in d.iteritems():
            if value == freq:
                count += 1

        return max(count, len(tasks))
