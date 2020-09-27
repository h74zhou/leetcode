class Solution(object):
    def subsets(self, nums):
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
                answer.append(currArr[:])
                for i in range(currIndex, len(nums)):
                    backtrack(currArr + [nums[i]], i + 1)

        backtrack([], 0)
        return answer
