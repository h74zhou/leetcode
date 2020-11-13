class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
         # find the pivot
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid

        # if the number is within pivot and right, search in this interval
        if nums[left] <= target <= nums[len(nums) - 1]:
            start, end = left, len(nums) - 1
        else:
            # otherwise, serach in other interval
            start, end = 0, left - 1

        # conduct regular binary search
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1
