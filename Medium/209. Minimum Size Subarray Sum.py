class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        minLength = float('inf')  # min length of contiguous subarray
        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]

            while currSum >= s:
                minLength = min(minLength, i + 1 - left)
                currSum -= nums[left]
                left += 1

        return minLength if minLength != float('inf') else 0
