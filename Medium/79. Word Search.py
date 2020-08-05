class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(currBoard, currRow, currColumn, currWord, currIndex):
            if currWord == word:
                return True

            if len(currWord) >= len(word):
                return False

            if currRow < 0 or currRow >= len(board) or currColumn < 0 or currColumn >= len(board[0]) or board[currRow][currColumn] != word[currIndex]:
                return False

            temp = board[currRow][currColumn]
            currBoard[currRow][currColumn] = ' '

            canContinue = dfs(currBoard[:], currRow - 1, currColumn, currWord + temp, currIndex + 1) or dfs(currBoard[:], currRow + 1, currColumn, currWord + temp, currIndex + 1) or dfs(currBoard[:], currRow, currColumn - 1, currWord + temp, currIndex + 1) or dfs(currBoard[:], currRow, currColumn + 1, currWord + temp, currIndex + 1)

            currBoard[currRow][currColumn] = temp
            return canContinue

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and dfs(board, row, column, "", 0):
                    return True
        return False
