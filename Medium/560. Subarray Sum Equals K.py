class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sumFound = {0: 1}

        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            # determine number of times preSum - k has occurred
            if currSum - k in sumFound:
                count += sumFound[currSum - k]

            if currSum not in sumFound:
                sumFound[currSum] = 1
            else:
                sumFound[currSum] += 1

        return count

