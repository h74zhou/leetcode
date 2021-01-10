class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # arr = [2, 3, 4, 7, 11]
        # arr2 = [1, 1, 1, 3, 6]

        left, right, mid = 0, len(arr), 0
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] - mid - 1 >= k:
                # min k satisfies arr2[i] >= k
                right = mid
            else:
                left = mid + 1

        return left + k
