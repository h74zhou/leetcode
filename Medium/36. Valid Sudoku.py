class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        map = {}
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == ".":
                    continue
                else:
                    rowStr = "Row: " + str(row) + " has digit: " + str(board[row][column])
                    columnStr = "Column: " + str(column) + " has digit: " + str(board[row][column])
                    gridStr = "Grid: " + str(row / 3) + ", " + str(column / 3) + ", hash digit: " + str(board[row][column])
                    if rowStr in map or columnStr in map or gridStr in map:
                        return False
                    map[rowStr] = 1
                    map[columnStr] = 1
                    map[gridStr] = 1
        return True
