class Solution(object):
    def sumOfDigits(self, n):
        total = 0
        while n != 0:
            digit = n % 10
            total += digit * digit
            n /= 10
        return total

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = self.sumOfDigits(n)
        fast = self.sumOfDigits(slow)

        while slow != fast:
            slow = self.sumOfDigits(slow)
            fast = self.sumOfDigits(fast)
            fast = self.sumOfDigits(fast)

        if slow == 1 and fast == 1:
            return True
        return False
