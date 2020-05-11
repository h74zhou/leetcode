class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        def backtrack(tempList, start):
            results.append(tempList)
            for i in range(start, len(nums)):
                tempList.append(nums[i])
                backtrack(tempList[:], i + 1)
                tempList.pop()

        nums.sort()
        backtrack([], 0)
        return results
