class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftArray = []
        leftArray.append(1)

        for i in range(1, len(nums)):
            leftArray.append(leftArray[i - 1] * nums[i - 1])

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            leftArray[i] *= right
            right *= nums[i]

        return leftArray
