class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        answer = []

        def backtrack(currArr, currIndex):
            answer.append(currArr)
            for i in range(currIndex, length):
                if i > currIndex and nums[i] == nums[i - 1]:
                    continue
                currArr.append(nums[i])
                backtrack(currArr[:], i + 1)
                currArr.pop()

        backtrack([], 0)
        return answer
