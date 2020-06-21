class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = set()
        answer = []

        for arr in matrix:
            row.add(min(arr))

        for i in range(len(matrix[0])):
            currMax = float('-inf')
            for j in range(len(matrix)):
                if matrix[j][i] >= currMax:
                    currMax = matrix[j][i]
            if currMax in row:
                answer.append(currMax)

        return answer
