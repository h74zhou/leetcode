class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for letter in magazine:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1

        for letter in ransomNote:
            if letter in d and d[letter] > 0:
                d[letter] -= 1
            else:
                return False

        return True
