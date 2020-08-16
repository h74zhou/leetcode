class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, length, right = 0, len(nums), len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        maxIndex = left + (length / 2)
        return True if maxIndex < len(nums) and nums[maxIndex] == target else False
