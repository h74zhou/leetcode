class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        d = {}
        for num in arr1:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        answer = []
        for num in arr2:
            if num in d:
                for i in range(d[num]):
                    answer.append(num)
                d.pop(num, None)

        last = []
        for index, val in d.iteritems():
            for i in range(val):
                last.append(index)

        last.sort()
        return answer + last
