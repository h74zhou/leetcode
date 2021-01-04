class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        perm = []

        def backtrack(currArr, visited):
            if visited == n:
                if len(currArr) == n:
                    perm.append(currArr)
            else:
                for i in range(1, n + 1):
                    if i in currArr:
                        continue
                    if i % (len(currArr) + 1) != 0 and (len(currArr) + 1) % i != 0:
                        continue
                    else:
                        backtrack(currArr[:] + [i], visited + 1)

        backtrack([], 0)
        return len(perm)

