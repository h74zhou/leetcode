class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0 or len(B) == 0:
            return []

        i, j, answer = 0, 0, []

        while i < len(A) and j < len(B):
            front = max(A[i][0], B[j][0])
            back = min(A[i][1], B[j][1])
            if back >= front:
                answer.append([front, back])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return answer
