import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # bucket[i] represent an array of elements with frequency of i
        bucket = [None for x in range(len(nums) + 1)]
        freq = {}
        answer = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, freqAmt in freq.iteritems():
            if bucket[freqAmt] is None:
                bucket[freqAmt] = [key]
            else:
                bucket[freqAmt].append(key)

        curr, count = len(bucket) - 1, 0
        while curr >= 0 and count < k:
            if bucket[curr] is not None:
                for num in bucket[curr]:
                    answer.append(num)
                    count += 1
            curr -= 1

        return answer


