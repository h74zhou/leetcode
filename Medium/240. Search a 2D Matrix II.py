class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        def binSearch(rowIndex):
            left, right = 0, len(matrix[rowIndex]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[rowIndex][mid] == target:
                    return True
                elif target < matrix[rowIndex][mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        for i in range(len(matrix)):
            if binSearch(i):
                return True
        return False
