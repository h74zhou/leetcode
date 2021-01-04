class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # find the longest contiguous subarray with <= K zeros
        if len(A) == 0:
            return 0
        start, end, longest = 0, 0, 0
        numOfZeros = 1 if A[0] == 0 else 0

        while start < len(A) and end < len(A):
            if numOfZeros <= K:
                longest = max(longest, end - start + 1)
                end += 1
                if end < len(A) and A[end] == 0:
                    numOfZeros += 1
            else:
                if A[start] == 0:
                    numOfZeros -= 1
                start += 1

        return longest
