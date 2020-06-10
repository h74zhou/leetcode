class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        d = {}
        for index, letter in enumerate(order):
            d[letter] = index

        def compareLex(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
                if word1[i] == word2[i]:
                    i += 1
                elif d[word1[i]] > d[word2[i]]:
                    return False
                else:
                    return True

            if len(word1) <= len(word2):
                return True
            return False

        for i in range(1, len(words)):
            if not compareLex(words[i - 1], words[i]):
                return False

        return True
