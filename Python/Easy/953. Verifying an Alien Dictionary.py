class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = {}
        for index, value in enumerate(order):
            d[value] = index

        def before(word1, word2):
            w1 = 0
            w2 = 0
            while w1 < len(word1) and w2 < len(word2):
                if d[word1[w1]] < d[word2[w2]]:
                    return True
                if d[word1[w1]] > d[word2[w2]]:
                    return False
                else:
                    w1 += 1
                    w2 += 1

            if len(word1) <= len(word2):
                return True
            return False

        for i in range(1, len(words)):
            if not before(words[i - 1], words[i]):
                return False

        return True
