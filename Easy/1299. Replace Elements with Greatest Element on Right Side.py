class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        i = len(arr) - 1
        currMax = arr[i]
        while i >= 0:
            tempMax = currMax
            if arr[i] > currMax:
                currMax = arr[i]
            arr[i] = tempMax
            i -= 1

        arr[len(arr) - 1] = -1
        return arr
