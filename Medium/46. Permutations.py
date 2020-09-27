class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        if len(nums) == 0:
            return answer

        nums.sort()

        def backtrack(currArr):
            if len(currArr) >= len(nums):
                answer.append(currArr[:])
            else:
                for i in range(len(nums)):
                    if nums[i] in currArr:
                        continue
                    else:
                        backtrack(currArr + [nums[i]])

        backtrack([])
        return answer
