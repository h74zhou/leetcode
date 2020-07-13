class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = {}
        for i in range(len(order)):
            d[order[i]] = i

        def before(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if d[word1[i]] < d[word2[i]]:
                    return True
                elif d[word1[i]] > d[word2[i]]:
                    return False
            return len(word1) <= len(word2)

        for i in range(1, len(words)):
            if not before(words[i - 1], words[i]):
                return False

        return True
