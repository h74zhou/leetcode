class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        answer = []

        def backtrack(currArr, currIndex):
            if len(currArr) >= k:
                answer.append(currArr[:])
            else:
                for i in range(currIndex, n + 1):
                    backtrack(currArr + [i], i + 1)

        backtrack([], 1)
        return answer
