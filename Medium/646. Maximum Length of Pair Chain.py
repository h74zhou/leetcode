class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        curr = float('-inf')
        answer = 0

        for first, second in pairs:
            if first > curr:
                curr = second
                answer += 1

        return answer
