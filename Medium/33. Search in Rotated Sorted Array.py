class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find smallest element at pivot
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        # left will be the pivot
        pivot = left

        if nums[left] <= target <= nums[len(nums) - 1]:
            # binary search from pivot to end
            left, right = pivot, len(nums) - 1
        else:
            # binary search from 0 to pivot
            left, right = 0, pivot

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
