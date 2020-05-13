class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            d[i] = 1

        answer = []
        for i in range(1, len(nums) + 1):
            if i not in d:
                answer.append(i)

        return answer
