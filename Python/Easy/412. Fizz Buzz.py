import sys

class Solution(object):
    tempLst = []

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                self.tempLst.append("FizzBuzz")
            elif i % 3 == 0:
                self.tempLst.append("Fizz")
            elif i % 5 == 0:
                self.tempLst.append("Buzz")
            else:
                self.tempLst.append(str(i))

# test
test = Solution()
test.fizzBuzz(15)
print(test.tempLst)
