class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        s = set()
        for num in arr:
            s.add(num)

        count, curr = 0, 0
        while count < k:
            curr += 1
            if curr not in s:
                count += 1

        return curr
