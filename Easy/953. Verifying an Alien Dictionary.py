class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) <= 1:
            return True

        d = {}
        for index, letter in enumerate(order):
            d[letter] = index

        # returns true if word1 comes before word2 lexigraphically
        def before(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if d[word1[i]] > d[word2[i]]:
                    return False
                elif d[word1[i]] < d[word2[i]]:
                    return True
            return True if len(word1) <= len(word2) else False

        j = 1
        while j < len(words):
            if not before(words[j - 1], words[j]):
                return False
            j += 1

        return True
