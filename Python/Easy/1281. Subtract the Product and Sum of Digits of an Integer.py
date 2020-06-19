class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = 1
        sum = 0

        while n > 0:
            digit = n % 10
            product *= digit
            sum += digit
            n /= 10

        return product - sum
