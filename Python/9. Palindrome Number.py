class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        numStr = str(x)
        i = 0
        j = len(numStr) - 1

        while i <= j:
            if numStr[i] != numStr[j]:
                return False
            i += 1
            j -= 1

        return True
