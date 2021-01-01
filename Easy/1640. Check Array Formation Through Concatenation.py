class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """

        d = {}
        for piece in pieces:
            d[piece[0]] = piece

        createdArr = []
        i = 0
        while i < len(arr):
            val = d.get(arr[i], None)
            if val is not None:
                createdArr += val
                i += len(val)
            else:
                return False

        return arr == createdArr

