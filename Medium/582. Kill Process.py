import sys

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        d = {} # parent: [children] mapping

        for index, val in enumerate(ppid):
            d[val] = d.get(val, []) + [pid[index]]

        q, answer = [kill], []

        while q:
            process = q.pop()
            answer.append(process)
            children = d.get(process)
            if children:
                q += children

        return answer

pidTest = [1, 3, 10, 5]
ppidTest = [3, 0, 5, 3]
killTest = 5
expectedAnswer = [5, 10]

sol = Solution()
code = sol.killProcess(pidTest, ppidTest, killTest)

print "Test Passed" if code == expectedAnswer else "Test Failed"
