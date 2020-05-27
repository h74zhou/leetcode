class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []

        def backtrack(currStr, left, right):
            if left == n and right == n:
                answer.append(currStr)
            else:
                if left == n:
                    backtrack(currStr + ")", left, right + 1)
                elif left >= right:
                    backtrack(currStr + "(", left + 1, right)
                    backtrack(currStr + ")", left, right + 1)

        backtrack("", 0, 0)
        return answer
