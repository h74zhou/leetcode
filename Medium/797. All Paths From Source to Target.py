from collections import deque

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        goal, q, answer = len(graph) - 1, deque(), []
        q.append([0])

        while q:
            last = q.popleft()
            if last[-1] == goal:
                answer.append(last)
            else:
                for child in graph[last[-1]]:
                    q.append(last + [child])

        return answer









