class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        def invert(num):
            if num == 0:
                return 1
            else:
                return 0

        for a in A:
            i = 0
            j = len(a) - 1
            while i <= j:
                if i == j:
                    a[i] = invert(a[i])
                else:
                    a[i] = invert(a[i])
                    a[j] = invert(a[j])
                    a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        return A
