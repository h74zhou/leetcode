class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastGoodPosition = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= lastGoodPosition:
                lastGoodPosition = i

        return lastGoodPosition == 0
