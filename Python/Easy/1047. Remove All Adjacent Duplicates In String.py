class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) == 0:
            return S

        stack = [S[0]]

        for letter in S[1:]:
            if len(stack) == 0 or letter != stack[-1]:
                stack.append(letter)
            elif letter == stack[-1]:
                stack.pop()

        answer = ""

        for letter in stack:
            answer += letter

        return answer
