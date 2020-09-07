class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # reverse top-down
        i, j = 0, len(matrix) - 1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

        # swap based on x and y
        for x in range(len(matrix)):
            for y in range(x, len(matrix[0])):
                print x, y
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
