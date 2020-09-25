class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """

        i, answer = 1, 0

        while i * (i - 1) // 2 < N:
            if (N - i * (i - 1) // 2) % i == 0:
                answer += 1
            i += 1

        return answer
