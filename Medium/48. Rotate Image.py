class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Reverse up and down
        matrix.reverse()
        # Swap the symmetry
        for row in range(len(matrix)):
            for column in range(row + 1, len(matrix[0])):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
