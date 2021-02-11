class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {} 
        for index, val in enumerate(nums):
            complement = target - val
            if complement in d:
                return [d[complement], index]
            d[val] = index
        return -1