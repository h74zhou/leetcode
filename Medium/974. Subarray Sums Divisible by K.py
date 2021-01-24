class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        d = {0: 1}
        currSum, count = 0, 0

        for i, v in enumerate(A):
            currSum += v
            count += d.get(currSum % K, 0)
            d[currSum % K] = d.get(currSum % K, 0) + 1

        return count
