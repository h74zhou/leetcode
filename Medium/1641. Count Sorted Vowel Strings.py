class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, e, i, o, u = 1, 1, 1, 1, 1

        for x in range(n - 1):
            a = a + e + i + o + u
            e = e + i + o + u
            i = i + o + u
            o = o + u

        return a + e + i + o + u
