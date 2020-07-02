class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) == 0:
            return

        self.prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefixSum.append(self.prefixSum[i - 1] + nums[i])


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.prefixSum[j]

        return self.prefixSum[j] - self.prefixSum[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
