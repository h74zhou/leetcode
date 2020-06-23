class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return nums

        left = [1] * len(nums)
        leftSum = nums[0]
        for i in range(1, len(nums)):
            left[i] = leftSum
            leftSum *= nums[i]

        rightIndex = len(nums) - 1
        rightSum = nums[rightIndex]
        rightIndex -= 1

        while rightIndex >= 0:
            left[rightIndex] *= rightSum
            rightSum *= nums[rightIndex]
            rightIndex -= 1

        return left
