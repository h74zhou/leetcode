class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1

        first = 0
        second = 1

        for i in range(2, N + 1):
            temp = second
            second = first + second
            first = temp

        return second
