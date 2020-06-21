class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return 0

        end = -2
        currMax = float('-inf')

        for index, val in enumerate(nums):
            currMax = max(currMax, val)
            if val < currMax:
                end = index

        start = - 1
        currMin = float('inf')
        for index, val in reversed(list(enumerate(nums))):
            currMin = min(currMin, val)
            if val > currMin:
                start = index

        return end - start + 1
