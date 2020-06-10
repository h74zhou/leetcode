class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        d = {}

        bCount = 0
        aCount = 0
        lCount = 0
        oCount = 0
        nCount = 0

        for c in text:
            if c == 'b':
                bCount += 1
            elif c == 'a':
                aCount += 1
            elif c == 'l':
                lCount += 1
            elif c == 'o':
                oCount += 1
            elif c == 'n':
                nCount += 1

        lCount = lCount / 2
        oCount = oCount / 2

        return min(bCount, aCount, lCount, oCount, nCount)
