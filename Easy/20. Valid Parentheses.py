class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for letter in s:
            if len(stack) == 0:
                stack.append(letter)
            else:
                if letter == '(' or letter == '{' or letter == '[':
                    stack.append(letter)
                elif letter == ')' and stack[-1] == '(':
                    stack.pop()
                elif letter == ']' and stack[-1] == '[':
                    stack.pop()
                elif letter == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(letter)

        return True if len(stack) == 0 else False
