class Solution(object):

    def isPalindrome(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return self.isPalindrome(s, start + 1, end) or self.isPalindrome(s, start, end - 1)
            else:
                start += 1
                end -= 1

        return True
