class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {} # val: index

        for index, val in enumerate(nums):
            complement = target - val
            complementIndex = d.get(complement, None)
            if complementIndex is not None:
                return [complementIndex, index]
            else:
                d[val] = index
        return []
