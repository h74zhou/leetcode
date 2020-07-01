class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        open = 0
        temp = ""

        for char in s:
            if char == '(':
                open += 1
            elif char == ')':
                if open == 0:
                    continue
                else:
                    open -= 1
            temp += char

        right = 0
        answer = ""
        for char in temp[::-1]:
            if char == '(':
                if right == 0:
                    continue
                else:
                    right -= 1
            elif char == ')':
                right += 1
            answer += char

        return answer[::-1]
