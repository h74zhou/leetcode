class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for y in range(len(board)):
            for x in range(len(board[0])):
                if (board[y][x] == 'X' and (y == 0 or board[y - 1][x] != 'X') and (x == 0 or board[y][x - 1] != 'X')):
                    count += 1
        return count
