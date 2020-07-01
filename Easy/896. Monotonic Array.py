class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True

        increasing = True
        decreasing = True

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                decreasing = False
            if A[i] < A[i - 1]:
                increasing = False

        return increasing or decreasing
