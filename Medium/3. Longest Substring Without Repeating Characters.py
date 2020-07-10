class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = {}
        maxLength = 0
        i = 0

        for j in range(len(s)):
            if s[j] not in window:
                window[s[j]] = 1
            else:
                while s[j] in window and i < j:
                    window.pop(s[i], None)
                    i += 1
                window[s[j]] = 1
            maxLength = max(maxLength, j - i + 1)

        return maxLength
