class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        start = float('-inf')
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                start = i
                break

        if start == float('-inf'):
            nums.reverse()
        else:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > nums[start]:
                    nums[i], nums[start] = nums[start], nums[i]
                    nums[start + 1: len(nums)] = nums[len(nums) - 1: start: -1]
                    break
