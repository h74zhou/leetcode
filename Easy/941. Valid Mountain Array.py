class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False

        increasing = True
        increased = 0
        decreased = 0

        for i in range(1, len(A)):
            if increasing:
                if A[i - 1] < A[i]:
                    increased += 1
                    continue
                elif A[i - 1] == A[i]:
                    return False
                else:
                    increasing = False
                    decreased += 1
            else:
                if A[i - 1] > A[i]:
                    decreased += 1
                    continue
                elif A[i - 1] == A[i]:
                    return False
                else:
                    return False

        return increasing == False and increased > 0 and decreased > 0
