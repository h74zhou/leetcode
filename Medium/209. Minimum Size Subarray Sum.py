class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        start, end, currSum, minSize = 0, 0, nums[0], float('inf')

        while end < len(nums):
            if currSum >= s:
                minSize = min(minSize, end - start + 1)
                if start < end:
                    currSum -= nums[start]
                    start += 1
                else:
                    start += 1
                    end += 1
                    if end < len(nums):
                        currSum = nums[end]
            else:
                end += 1
                if end < len(nums):
                    currSum += nums[end]

        return minSize if minSize != float('inf') else 0
