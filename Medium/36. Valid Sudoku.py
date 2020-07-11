class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr != ".":
                    rowCheck = "currElement: " + curr + " in row: " + str(i)
                    columnCheck = "currElement: " + curr + " in column: " + str(j)
                    boxCheck = "currElement: " + curr + " in box " + str(i / 3) + " : " + str(j / 3)
                    if rowCheck in d or columnCheck in d or boxCheck in d:
                        return False
                    d.add(rowCheck)
                    d.add(columnCheck)
                    d.add(boxCheck)

        return True
