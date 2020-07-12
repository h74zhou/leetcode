class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        answer = []

        while i < len(A) and j < len(B):
            aStart, aEnd = A[i]
            bStart, bEnd = B[j]

            if aStart <= bEnd and aEnd >= bStart:
                answer.append([max(aStart, bStart), min(aEnd, bEnd)])

            if aEnd <= bEnd:
                i += 1
            else:
                j += 1

        return answer
