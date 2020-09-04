class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getDigitSum(num):
            digitSum = 0
            while num:
                digitSum += (num % 10) * (num % 10)
                num /= 10
            return digitSum

        slow = getDigitSum(n)
        if slow == 1:
            return True

        fast = getDigitSum(slow)
        if fast == 1:
            return True

        while slow != fast and slow != 1 and fast != 1:
            slow = getDigitSum(slow)
            fast = getDigitSum(fast)
            fast = getDigitSum(fast)

        return True if slow == 1 or fast == 1 else False
