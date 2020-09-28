class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        answer = []

        def isPalindrome(word):
            start, end = 0, len(word) - 1
            while start <= end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(currArr, currIndex):
            if currIndex >= len(s):
                answer.append(currArr[:])
            else:
                for i in range(currIndex, len(s)):
                    if isPalindrome(s[currIndex:i + 1]):
                        backtrack(currArr[:] + [s[currIndex:i + 1]], i + 1)

        backtrack([], 0)
        return answer
