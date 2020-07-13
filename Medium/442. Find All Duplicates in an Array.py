class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for i in range(len(nums)):
            curr = abs(nums[i])
            if nums[curr - 1] < 0:
                answer.append(curr)
            else:
                nums[curr - 1] *= -1

        return answer
