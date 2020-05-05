class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return nums[0]

        localMax = float('-inf')
        globalMax = float('-inf')

        for num in nums:
            localMax = max(num, localMax + num)
            if localMax > globalMax:
                globalMax = localMax

        return globalMax
