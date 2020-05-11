class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        def backtrack(tempList):
            if len(tempList) == len(nums):
                results.append(tempList)
            else:
                for i in range(len(nums)):
                    if nums[i] in tempList:
                        continue
                    else:
                        tempList.append(nums[i])
                        backtrack(tempList[:])
                        tempList.pop()

        backtrack([])
        return results
