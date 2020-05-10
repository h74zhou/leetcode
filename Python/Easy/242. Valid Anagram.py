class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        for c in t:
            if c not in dict:
                return False
            else:
                dict[c] -= 1
                if dict[c] == 0:
                    dict.pop(c, None)

        return not bool(dict)
