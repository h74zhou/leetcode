class Solution(object):
    def candyCrush(self, board):
        boardChanged = True

        while boardChanged:
            boardChanged = False

            # crush horizontally
            for r in range(len(board)):
                for c in range(len(board[0]) - 2):
                    num1, num2, num3 = abs(board[r][c]), abs(board[r][c + 1]), abs(board[r][c + 2])
                    if num1 == num2 == num3 != 0:
                        board[r][c], board[r][c + 1], board[r][c + 2] = -num1, -num2, -num3
                        boardChanged = True

            # crush vertically
            for c in range(len(board[0])):
                for r in range(len(board) - 2):
                    num1, num2, num3 = abs(board[r][c]), abs(board[r + 1][c]), abs(board[r + 2][c])
                    if num1 == num2 == num3 != 0:
                        board[r][c], board[r + 1][c], board[r + 2][c] = -num1, -num2, -num3
                        boardChanged = True

            # let blocks fall
            for c in range(len(board[0])):
                lastNonPostive = len(board) - 1

                # move all positive numbers down
                for r in range(len(board) - 1, -1, -1):
                    if board[r][c] > 0:
                        board[r][c], board[lastNonPostive][c] = board[lastNonPostive][c], board[r][c]
                        lastNonPostive -= 1

                # put zeros for missing blocks
                for r in range(lastNonPostive, -1, -1):
                    board[r][c] = 0

        return board

board = [[110,5,112,113,114],
         [210,211,5,213,214],
         [310,311,3,313,314],
         [410,411,412,5,414],
         [5,1,512,3,3],
         [610,4,1,613,614],
         [710,1,2,713,714],
         [810,1,2,1,1],
         [1,1,2,2,2],
         [4,1,4,4,1014]
        ]

answer = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [110,0,0,0,114],
          [210,0,0,0,214],
          [310,0,0,113,314],
          [410,0,0,213,414],
          [610,211,112,313,614],
          [710,311,412,613,714],
          [810,411,512,713,1014]
         ]

instance = Solution()
finishedBoard = instance.candyCrush(board)
if finishedBoard == answer:
    print "success"
else:
    print "fail"
