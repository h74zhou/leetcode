class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []

        # left, right represent current left and right amount of brackets
        def backtrack(currStr, left, right):
            if left == n and right == n:
                answer.append(currStr[:])
            else:
                if left == right:
                    backtrack(currStr + '(', left + 1, right)
                elif left > right and left < n:
                    backtrack(currStr + '(', left + 1, right)
                    backtrack(currStr + ')', left, right + 1)
                elif left > right and left == n:
                    backtrack(currStr + ')', left, right + 1)

        backtrack("", 0, 0)
        return answer
