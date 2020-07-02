class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0:
            return
        self.matrixSum = [[0 for x in range(len(matrix[0]) + 1)] for y in range(len(matrix) + 1)]

        for y in range(1, len(matrix) + 1):
            for x in range(1, len(matrix[0]) + 1):
                self.matrixSum[y][x] = matrix[y - 1][x - 1] + self.matrixSum[y - 1][x] + self.matrixSum[y][x - 1] - self.matrixSum[y - 1][x - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.matrixSum[row2][col2] - self.matrixSum[row2][col1 - 1] - self.matrixSum[row1 - 1][col2] + self.matrixSum[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
