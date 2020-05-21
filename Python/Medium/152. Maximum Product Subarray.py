class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return nums[0]

        globalMax = nums[0]
        localMax = nums[0]
        localMin = nums[0]

        for i in range(1, len(nums)):
            prevMax = localMax
            prevMin = localMin
            localMax = max(nums[i], nums[i] * prevMax, nums[i] * prevMin)
            localMin = min(nums[i], nums[i] * prevMax, nums[i] * prevMin)
            globalMax = max(localMax, globalMax, localMin)
            # print localMax, localMin, globalMax

        return globalMax
