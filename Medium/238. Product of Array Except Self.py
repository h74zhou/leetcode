class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return nums

        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]

        j = len(nums) - 1
        right = 1

        while j >= 0:
            left[j] = left[j] * right
            right *= nums[j]
            j -= 1

        return left
