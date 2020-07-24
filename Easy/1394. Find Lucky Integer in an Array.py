class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        maxLucky = float('-inf')
        for num, freq in d.iteritems():
            if num == freq and freq > maxLucky:
                maxLucky = num

        return maxLucky if maxLucky != float('-inf') else -1
