class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.memo = {}

        def dp(currIndex, currSum):
            if (currIndex, currSum) in self.memo:
                return self.memo[(currIndex, currSum)]

            if currIndex < 0 and currSum == S:
                return 1
            elif currIndex < 0 and currSum != S:
                return 0

            positive = dp(currIndex - 1, currSum + nums[currIndex])  # take the positive at this index
            negative = dp(currIndex - 1, currSum - nums[currIndex])  # take the negative at this index

            self.memo[(currIndex, currSum)] = positive + negative
            return positive + negative  # return ways to get S when taking negative or positive at this index

        return dp(len(nums) - 1, 0)
