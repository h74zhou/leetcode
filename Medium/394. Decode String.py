class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        currNum, currStr, stack = 0, "", []

        for c in s:
            if c == "[":
                stack.append(currStr)
                stack.append(currNum)
                currNum = 0
                currStr = ""
            elif c == "]":
                prevNum = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + prevNum * currStr
            elif c.isdigit():
                currNum = currNum * 10 + int(c)
            else:
                currStr += c

        return currStr
