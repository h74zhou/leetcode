class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False

        prefixSum = 0
        d = {0: -1}

        for i in range(len(nums)):
            prefixSum += nums[i]
            prefixSum = prefixSum % k if k != 0 else prefixSum
            if prefixSum in d:
                if i - d[prefixSum] > 1:
                    return True
            else:
                d[prefixSum] = i

        return False
