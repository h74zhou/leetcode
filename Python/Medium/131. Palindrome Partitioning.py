class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        answer = []

        def isPalindrome(string):
            i = 0
            j = len(string) - 1
            while i < j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(currStr, currArr, currIndex):
            if currIndex == len(s):
                return
            else:
                for i in range(currIndex, len(s)):
                    if isPalindrome(currStr):
                        currArr.append(currStr)
                        backtrack(currStr + s[i], currArr[:], i + 1)

        backtrack("", [], 0)
        return answer
