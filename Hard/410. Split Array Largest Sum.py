class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # can nums be split into m parts, such that every sum(part) <= limit (returns True if yes, else False)
        def feasible(limit):
            currVal, count = 0, 1
            for num in nums:
                currVal += num
                if currVal > limit:
                    count += 1
                    currVal = num
                    if count > m:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
