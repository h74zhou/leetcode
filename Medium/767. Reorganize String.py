class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        # use heap
        d = {}
        mFreq = 0
        for c in S:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
            if d[c] > mFreq:
                mFreq = d[c]
