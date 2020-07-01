class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        def dfs(y, x):
            if y < 0 or y >= len(grid):
                return 0
            if x < 0 or x >= len(grid[0]):
                return 0
            if grid[y][x] == '0':
                return 0
            grid[y][x] = '0'
            dfs(y + 1, x)
            dfs(y - 1, x)
            dfs(y, x + 1)
            dfs(y, x - 1)
            return 1

        row = len(grid)
        column = len(grid[0])
        count = 0

        for y in range(row):
            for x in range(column):
                count += dfs(y, x)

        return count
