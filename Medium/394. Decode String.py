class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, currStr, currCount = [], "", 0

        for letter in s:
            if letter == "[":
                stack.append(currStr)
                stack.append(currCount)
                currStr = ""
                currCount = 0
            elif letter == "]":
                prevCount = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + prevCount * currStr
            elif letter.isdigit():
                currCount = currCount * 10 + int(letter)
            else:
                currStr += letter

        return currStr


