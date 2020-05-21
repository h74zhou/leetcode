class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return [-1, -1]

        left = 0
        right = length - 1

        while left <= right:
            mid = (left + right) / 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        left2 = 0
        right2 = length - 1
        while left2 <= right2:
            mid = (left2 + right2) / 2
            if nums[mid] <= target:
                left2 = mid + 1
            else:
                right2 = mid - 1

        return [left, right2] if left <= right2 else [-1, -1]
