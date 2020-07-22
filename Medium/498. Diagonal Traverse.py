class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        if row == 0:
            return []
        column = len(matrix[0])
        arr, n, r, c, = [], row * column, 0, 0

        for i in range(n):
            arr.append(matrix[r][c])
            if (r + c) % 2 == 0:
                if c == column - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == row - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return arr
