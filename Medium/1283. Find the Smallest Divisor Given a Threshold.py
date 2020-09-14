class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def condition(divisor):
            totalSum = 0
            for num in nums:
                totalSum += (num + divisor - 1) // divisor
            if totalSum <= threshold:
                return True
            return False

        left, right = 1, max(nums)

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left
