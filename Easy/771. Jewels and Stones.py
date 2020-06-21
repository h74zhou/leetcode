class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel = {}
        for i in J:
            if i not in jewel:
                jewel[i] = 1

        count = 0
        for s in S:
            if s in jewel:
                count += 1

        return count
