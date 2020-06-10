class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            indexS = -1 if s[i] not in sMap else sMap[s[i]]
            indexT = -1 if t[i] not in tMap else tMap[t[i]]

            if indexS != indexT:
                return False

            sMap[s[i]] = i
            tMap[t[i]] = i

        return True
