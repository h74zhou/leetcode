# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i <= j:
            mid = (i + j) / 2
            curr = isBadVersion(mid)
            prev = isBadVersion(mid - 1)
            if curr and not prev:
                return mid
            elif curr and prev:
                j = mid - 1
            elif not curr:
                i = mid + 1

        return 0
