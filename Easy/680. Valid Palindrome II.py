class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        if len(s) <= 1:
            return True
        start, end = 0, len(s) - 1
        while start <= end:
            if s[start] != s[end]:
                return isPalindrome(start, end - 1) or isPalindrome(start + 1, end)
            start += 1
            end -= 1
        return True
