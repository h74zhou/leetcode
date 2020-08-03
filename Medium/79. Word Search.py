class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        map = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                letter = board[i][j]
                if letter in map:
                    map[letter].append((i, j))
                else:
                    map[letter] = [(i, j)]

        def backtrack(currWord, currIndex, row, col, used):
            print "current hashmap"
            print used
            print "current index"
            print(row, col)
            if currWord == word:
                return True
            else:
                if row + 1 < len(board) and board[row + 1][col] == word[currIndex] and (row + 1, col) not in used:
                    used[(row, col)] = 1
                    return backtrack(currWord + word[currIndex], currIndex + 1, row + 1, col, used.copy())
                if row - 1 >= 0 and board[row - 1][col] == word[currIndex] and (row - 1, col) not in used:
                    used[(row, col)] = 1
                    return backtrack(currWord + word[currIndex], currIndex + 1, row - 1, col, used.copy())
                if col + 1 < len(board[0]) and board[row][col + 1] == word[currIndex] and (row, col + 1) not in used:
                    used[(row, col)] = 1
                    return backtrack(currWord + word[currIndex], currIndex + 1, row, col + 1, used.copy())
                if col - 1 >= 0 and board[row][col - 1] == word[currIndex] and (row, col - 1) not in used:
                    used[(row, col)] = 1
                    return backtrack(currWord + word[currIndex], currIndex + 1, row, col - 1, used.copy())

        if word[0] not in map:
            return False
        indexArr = map[word[0]]

        for row, col in indexArr:
            print "new starting point"
            print(row, col)
            if backtrack(word[0], 1, row, col, {}) == True:
                return True
        return False
