class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        longest = 0
        window = {}
        left = 0

        for right in range(len(s)):
            if s[right] in window:
                left = max(left, window.get(s[right]) + 1)
            window[s[right]] = right
            longest = max(longest, right - left + 1)

        return longest
