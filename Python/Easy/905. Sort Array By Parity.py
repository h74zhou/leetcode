class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 0:
            return A

        i = 0
        j = len(A) - 1

        while i < j:
            if A[i] % 2 != 0 and A[j] % 2 == 0:
                # i is odd (1), j is even (0)
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            elif A[i] % 2 == 0:
                # i is even (0), move i up
                i += 1
            elif A[j] % 2 == 0 and A[i] % 2 != 0:
                # if j is even and i is not even, swap
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            elif A[j] % 2 != 0 and A[i] % 2 != 0:
                j -= 1

        return A
