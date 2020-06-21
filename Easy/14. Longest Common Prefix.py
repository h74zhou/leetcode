class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        first = strs[0]
        curr = ""
        for i in range(len(first)):
            letter = first[i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    return curr
                if strs[j][i] != letter:
                    return curr
            curr += letter
        return curr
