import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i] = 0 - nums[i]
        heapq.heapify(nums)

        answer = 0
        for i in range(k):
            answer = heapq.heappop(nums)

        return answer * -1
