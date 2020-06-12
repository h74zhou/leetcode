class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        stack = []
        for letter in reversed(s):
            stack.append(letter)

        for letter in t:
            if len(stack) == 0:
                return True
            if letter == stack[-1]:
                stack.pop()

        return len(stack) == 0
