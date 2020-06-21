class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False

        value = sum(nums) / 2
        dp = [[False for x in range(value + 1)] for y in range(len(nums) + 1)]
        dp[0][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(value + 1):
                dp[i][j] = dp[i - 1][j]
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]
