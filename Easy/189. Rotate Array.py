class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverseIndex(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        while k >= len(nums):
            k -= len(nums)

        if k != 0 and len(nums) > 1:
            nums.reverse()
            reverseIndex(0, k - 1)
            reverseIndex(k, len(nums) - 1)
