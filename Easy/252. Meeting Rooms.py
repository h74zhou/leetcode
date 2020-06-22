class Solution(object):
    def canAttendMeetings(self, nums):
        """
        :type nums: List[int]
        :rtype: Boolean
        """
        start = nums[0][0]
        end = nums[0][1]

        for s, e in nums[1:]:
            front = max(s, start)
            back = min(e, end)
            if back - front >= 0:
                return False
        return True


answer = Solution()
print answer.canAttendMeetings([[1, 4], [5, 6], [8, 9]])
