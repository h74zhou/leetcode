class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        mySet = set()
        for index, val in d.iteritems():
            if val in mySet:
                return False
            mySet.add(val)

        return True
