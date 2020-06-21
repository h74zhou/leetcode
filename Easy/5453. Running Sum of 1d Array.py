class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums
