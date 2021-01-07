class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        start, end, currProduct, count = 0, 0, 1, 0

        while end < len(nums):
            currProduct *= nums[end]

            while currProduct >= k:
                currProduct /= nums[start]
                start += 1

            count += end - start + 1
            end += 1

        return count

