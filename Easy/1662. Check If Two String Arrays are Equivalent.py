class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        first, second = "", ""

        for word in word1:
            first += word
        for word in word2:
            second += word

        return first == second
