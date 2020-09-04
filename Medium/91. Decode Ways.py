class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i] represents # of ways to decode message at length i
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        if s[0] == '0':
            return 0

        for i in range(2, len(dp)):
            oneDigit = int(s[i - 1: i])
            twoDigit = int(s[i - 2: i])

            if 0 < oneDigit <= 9:
                dp[i] += dp[i - 1]

            if 10 <= twoDigit <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
