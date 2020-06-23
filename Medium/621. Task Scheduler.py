class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = {}
        mostFreq = float('-inf')
        for task in tasks:
            if task in d:
                d[task] += 1
            else:
                d[task] = 1
            if d[task] >= mostFreq:
                mostFreq = d[task]

        answer = (mostFreq - 1) * (n + 1)

        for task, freq in d.iteritems():
            if freq == mostFreq:
                answer += 1

        return max(len(tasks), answer)
