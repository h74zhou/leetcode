class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d, pairs = {}, 0
        for num in nums:
            d[num] = d.get(num, 0) + 1

        for key, val in d.iteritems():
            if k == 0:
                if val >= 2:
                    pairs += 1
            else:
                if d.get(key + k):
                    pairs += 1

        return pairs


