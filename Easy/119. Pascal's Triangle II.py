class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = []
        numRows = rowIndex + 1

        if numRows == 0:
            return [1]

        if numRows >= 1:
            triangle.append([1])

        if numRows >= 2:
            triangle.append([1, 1])

        for i in range(2, numRows):
            row = []
            row.append(1)

            for j in range(1, len(triangle[i - 1])):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)

        return triangle[rowIndex]
