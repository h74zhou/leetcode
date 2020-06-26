class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low = 0
        high = len(A) - 1

        while low <= high:
            mid = (high + low) / 2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                return mid
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                low = mid + 1
            elif A[mid - 1] > A[mid] > A[mid + 1]:
                high = mid - 1

        return low
