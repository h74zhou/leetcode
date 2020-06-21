class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num == 2 or num == 3:
            return False

        l = 1
        r = num

        while l <= r:
            mid = (l + r) / 2
            squared = mid * mid

            if squared == num:
                return True
            elif squared < num:
                l = mid + 1
            elif squared > num:
                r = mid - 1

        return False
