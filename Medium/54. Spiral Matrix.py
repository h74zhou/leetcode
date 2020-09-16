class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []

        m, n, answer = len(matrix[0]), len(matrix), []
        left, top, right, bottom = 0, 0, m - 1, n - 1

        while len(answer) < m * n:
            for i in range(left, m):
                if len(answer) < m * n:
                    answer.append(matrix[top][i])
            top += 1

            for i in range(top, right + 1):
                if len(answer) < m * n:
                    answer.append(matrix[i][right])
            right -= 1

            for i in range(right, bottom - 1, -1):
                if len(answer) < m * n:
                    answer.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, left - 1, -1):
                if len(answer) < m * n:
                    answer.append(matrix[i][left])
            left += 1

        return answer
