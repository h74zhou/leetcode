class Solution(object):
    def canAttendMeetings(self, meetings):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        meetings.sort()
        for i in range(1, len(meetings)):
            currStart = meetings[i][0]
            prevEnd = meetings[i - 1][1]
            if prevEnd > currStart:
                return False
        return True


test = Solution()
print test.canAttendMeetings([[0, 25], [30, 36], [26, 28]])
