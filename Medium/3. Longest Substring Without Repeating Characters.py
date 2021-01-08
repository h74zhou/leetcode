class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
#       s = "abcabcbb"
#       Output: 3
        start, longest = 0, 0
        d = {} # letter: last index of where it occured

        for end in range(len(s)):
            if s[end] in d:
                start = max(start, d[s[end]] + 1)
            d[s[end]] = max(d.get(s[end], 0), end)
            longest = max(longest, end - start + 1)

        return longest
