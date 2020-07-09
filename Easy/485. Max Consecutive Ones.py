class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxOnes, currOnes = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                currOnes += 1
            else:
                currOnes = 0
            maxOnes = max(currOnes, maxOnes)

        return maxOnes
