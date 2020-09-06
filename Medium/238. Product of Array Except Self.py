class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSum = [1]
        for i in range(1, len(nums)):
            leftSum.append(leftSum[i - 1] * nums[i - 1])

        rightSum = 1
        for i in range(len(nums) - 1, -1, -1):
            leftSum[i] *= rightSum
            rightSum *= nums[i]

        return leftSum
