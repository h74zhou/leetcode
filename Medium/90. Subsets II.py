class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        if len(nums) == 0:
            return answer

        nums.sort()

        def backtrack(currArr, currIndex):
            if len(currArr) > len(nums):
                return
            else:
                if currArr[:] not in answer:
                    answer.append(currArr[:])
                for i in range(currIndex, len(nums)):
                    backtrack(currArr + [nums[i]], i + 1)

        backtrack([], 0)
        return answer
