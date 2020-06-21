class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' or i == '}' or i == ']':
                if len(stack) == 0:
                    stack.append(i)
                elif match[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)

        return len(stack) == 0
