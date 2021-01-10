class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        wordPointer1, wordPointer2 = 0, 0
        letterPointer1, letterPointer2 = 0, 0

        while wordPointer1 < len(word1) and wordPointer2 < len(word2):
            if word1[wordPointer1][letterPointer1] != word2[wordPointer2][letterPointer2]:
                return False

            letterPointer1 += 1
            letterPointer2 += 1

            if letterPointer1 >= len(word1[wordPointer1]):
                letterPointer1 = 0
                wordPointer1 += 1

            if letterPointer2 >= len(word2[wordPointer2]):
                letterPointer2 = 0
                wordPointer2 += 1

        return True if wordPointer1 >= len(word1) and wordPointer2 >= len(word2) else False
