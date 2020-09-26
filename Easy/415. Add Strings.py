class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 0:
            return num2

        if len(num2) == 0:
            return num1

        int1, int2 = int(num1[-1]), int(num2[-1])
        if int1 + int2 < 10:
            return self.addStrings(num1[:-1], num2[:-1]) + str(int1 + int2)
        else:
            return self.addStrings(self.addStrings(num1[:-1], num2[:-1]), '1') + str(int1 + int2)[-1]

