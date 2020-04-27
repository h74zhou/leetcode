class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0
        numsLength = len(nums)
        for i in nums:
            if i != 0:
                nums[lastNonZero] = i
                lastNonZero += 1

        for i in range(lastNonZero, numsLength):
            nums[i] = 0

        return nums
