class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixSum = 0
        d = {0: 1}
        count = 0

        for i in range(len(nums)):
            prefixSum += nums[i]
            count += d.get(prefixSum - k, 0)
            d[prefixSum] = d.get(prefixSum, 0) + 1

        return count
