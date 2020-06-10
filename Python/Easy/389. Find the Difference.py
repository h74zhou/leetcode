class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        for c in t:
            if c not in d:
                return c
            else:
                d[c] -= 1

        for key, val in d.iteritems():
            if val != 0:
                return key

        return 0
