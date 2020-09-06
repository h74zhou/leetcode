class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True

        increasing = False
        decreasing = False

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                increasing = True
            elif A[i] < A[i - 1]:
                decreasing = True

        if increasing and decreasing:
            return False

        return True
