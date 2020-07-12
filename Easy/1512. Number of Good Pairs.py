class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        answer = 0
        for index, value in d.iteritems():
            answer += (value * (value - 1)) / 2

        return answer
