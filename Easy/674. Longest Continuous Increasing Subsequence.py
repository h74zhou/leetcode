class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        answer = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
                answer = max(answer, curr)
            else:
                curr = 1

        return answer
