class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        per = 0

        def inGrid(r, c):
            if not (r >= 0 and r < height and c >= 0 and c < width) or grid[r][c] == 0:
                return True
            return False

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 1 and inGrid(row, col - 1):
                    per += 1
                if grid[row][col] == 1 and inGrid(row - 1, col):
                    per += 1
                if grid[row][col] == 1 and inGrid(row, col + 1):
                    per += 1
                if grid[row][col] == 1 and inGrid(row + 1, col):
                    per += 1

        return per
