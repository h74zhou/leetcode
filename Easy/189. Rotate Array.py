class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def flip(start, end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1

        while k >= len(nums):
            k -= len(nums)

        flip(0, len(nums) - 1)
        flip(0, k - 1)
        flip(k, len(nums) - 1)
