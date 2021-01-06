class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0: 1}
        prefixSum = 0
        count = 0

        for num in nums:
            prefixSum += num
            count += d.get(prefixSum - k, 0)
            d[prefixSum] = d.get(prefixSum, 0) + 1

        return count
        [1, 0, 0]
