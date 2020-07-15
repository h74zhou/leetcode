class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s

        self.maxLength = float('-inf')
        self.begin = 0

        def check(start, end):
            while (start >= 0 and end < len(s)) and s[start] == s[end]:
                start -= 1
                end += 1

            if end - start - 1 > self.maxLength:
                self.maxLength = end - start - 1
                self.begin = start + 1

        for i in range(len(s)):
            check(i, i)
            check(i, i + 1)

        return s[self.begin: self.begin + self.maxLength]
