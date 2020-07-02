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

        if int(num1[-1]) + int(num2[-1]) >= 10:
            return self.addStrings(self.addStrings(num1[:-1], num2[:-1]), "1") + str(((int(num1[-1]) + int(num2[-1])) % 10))
        elif int(num1[-1]) + int(num2[-1]) < 10:
            return self.addStrings(num1[:-1], num2[:-1]) + str(int(num1[-1]) + int(num2[-1]))
