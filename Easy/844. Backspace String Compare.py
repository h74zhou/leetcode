class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stackS = []
        stackT = []

        for letter in S:
            if letter == "#":
                if len(stackS) > 0:
                    stackS.pop()
            else:
                stackS.append(letter)

        for letter in T:
            if letter == "#":
                if len(stackT) > 0:
                    stackT.pop()
            else:
                stackT.append(letter)

        return stackS == stackT
