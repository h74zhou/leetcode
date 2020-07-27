class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        newString = ""
        for word in s.split():
            newString = word + " " + newString
        return newString[:-1]
