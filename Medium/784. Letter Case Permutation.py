class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        answer = []
        if len(S) == 0:
            return answer

        def backtrack(currStr, currIndex):
            if currIndex >= len(S):
                answer.append(currStr[:])
            else:
                if S[currIndex].isdigit():
                    backtrack(currStr + S[currIndex], currIndex + 1)
                else:
                    backtrack(currStr + S[currIndex].lower(), currIndex + 1)
                    backtrack(currStr + S[currIndex].upper(), currIndex + 1)

        backtrack("", 0)
        return answer
