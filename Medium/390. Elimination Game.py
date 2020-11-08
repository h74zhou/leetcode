class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = True
        remain, head, step = n, 1, 1

        while remain > 1:
            if left:
                head += step
            else:
                if remain % 2 == 1:
                    head += step
            remain = remain / 2
            left = not left
            step *= 2

        return head
