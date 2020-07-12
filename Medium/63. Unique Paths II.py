class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for y in range(len(obstacleGrid[0]))] for x in range(len(obstacleGrid))]

        for x in range(len(obstacleGrid[0])):
            if obstacleGrid[0][x] == 0:
                dp[0][x] = 1
            else:
                break
        for y in range(len(obstacleGrid)):
            if obstacleGrid[y][0] == 0:
                dp[y][0] = 1
            else:
                break

        for y in range(1, len(obstacleGrid)):
            for x in range(1, len(obstacleGrid[0])):
                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0
                else:
                    dp[y][x] = dp[y - 1][x] + dp[y][x - 1]

        return dp[-1][-1]
