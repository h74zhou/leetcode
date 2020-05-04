class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        count = len(nums) / 2

        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1

            if map[i] > count:
                return i
        return
