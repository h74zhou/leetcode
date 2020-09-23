class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        numOfRows = len(matrix) - 1
        maxRowIndex = len(matrix[0]) - 1

        def inRow(rowIndex):
            return True if matrix[rowIndex][0] <= target <= matrix[rowIndex][maxRowIndex] else False

        left, right = 0, numOfRows

        while left <= right:
            mid = left + (right - left) // 2
            if inRow(mid):
                # Do binary search in row
                rowLeft, rowRight = 0, maxRowIndex
                while rowLeft <= rowRight:
                    rowMid = rowLeft + (rowRight - rowLeft) // 2
                    if matrix[mid][rowMid] == target:
                        return True
                    elif target < matrix[mid][rowMid]:
                        rowRight = rowMid - 1
                    else:
                        rowLeft = rowMid + 1
                return False
            elif target < matrix[mid][-1]:
                right = mid - 1
            else:
                left = mid + 1

        return False
