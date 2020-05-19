class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) / 2
            val = nums[mid]

            if val == target:
                return mid
            elif val > target:
                j = mid - 1
            elif val < target:
                i = mid + 1

        return -1
