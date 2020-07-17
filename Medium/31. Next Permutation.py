class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                k = i
                break

        if k == len(nums) - 1:
            nums.reverse()
            return

        for i in range(len(nums) - 1, -1, -1):
            if i > k and nums[i] > nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
                nums[k + 1: len(nums)] = nums[len(nums) - 1: k: -1]
                break
