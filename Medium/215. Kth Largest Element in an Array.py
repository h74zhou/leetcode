import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return None

        heapq.heapify(nums)

        for i in range(len(nums) - k + 1):
            answer = heapq.heappop(nums)

        return answer
