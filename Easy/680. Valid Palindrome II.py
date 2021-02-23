class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(word, start, end):
            while start < end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1
            return True

        start, end = 0, len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return isPalindrome(s, start + 1, end) or isPalindrome(s, start, end - 1)
            start += 1
            end -= 1

        return True
