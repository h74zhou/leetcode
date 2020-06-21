class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = {}
        for i in A:
            if i in d:
                return i
            else:
                d[i] = 1

        return 0
