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

        def backtrack(currArr, currIndex):
            if currIndex == len(s):
                answer.append(currArr)
            else:
                for i in range(currIndex, len(s)):
                    if isPalindrome(s[currIndex: i + 1]):
                        currArr.append(s[currIndex: i + 1])
                        backtrack(currArr[:], i + 1)
                        currArr.pop()

        backtrack([], 0)
        return answer
