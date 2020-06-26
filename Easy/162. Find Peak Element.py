class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == 0:
                low = float('-inf')
            else:
                low = nums[i - 1]
            if i == len(nums) - 1:
                high = float('-inf')
            else:
                high = nums[i + 1]

            if nums[i] > low and nums[i] > high:
                return i

        return 0
