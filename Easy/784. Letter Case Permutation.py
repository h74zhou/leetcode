class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        answer = []
        maxLength = len(S)

        def backtrack(currStr, currIndex):
            if len(currStr) == maxLength:
                answer.append(currStr)
                return

            if S[currIndex].isdigit():
                currStr += S[currIndex]
                backtrack(currStr, currIndex + 1)
                currStr = currStr[:-1]
            elif S[currIndex].isalpha():
                backtrack(currStr + S[currIndex].lower(), currIndex + 1)
                backtrack(currStr + S[currIndex].upper(), currIndex + 1)

        backtrack("", 0)
        return answer
