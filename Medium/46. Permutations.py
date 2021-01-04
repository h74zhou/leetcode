class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []

        if len(nums) == 0:
            return answer

        def backtrack(currArr, currIndex, currSet):
            if len(currArr) == len(nums):
                answer.append(currArr)
            else:
                for i in range(len(nums)):
                    if nums[i] in currSet:
                        continue
                    newSet = currSet.copy()
                    newSet.add(nums[i])
                    backtrack(currArr[:] + [nums[i]], i + 1, newSet)

        backtrack([], 0, set())
        return answer
