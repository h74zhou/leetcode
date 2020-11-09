class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """

        stack, answer = [], ""

        for letter in S:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)

        return answer.join(stack)
