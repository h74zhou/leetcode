class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        start, end, currSum, minLength = 0, 0, nums[0], float('inf')
        while start < len(nums) and end < len(nums):
            if currSum >= s:
                minLength = min(end - start + 1 , minLength)
                currSum -= nums[start]
                start += 1
            else:
                end += 1
                if end < len(nums):
                    currSum += nums[end]

        return minLength if minLength != float('inf') else 0


