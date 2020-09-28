class Solution(object):
    def meetingScheduler(self, slots1, slots2, duration):
        slots1.sort()
        slots2.sort()

        i, j = 0, 0

        while i < len(slots1) and j < len(slots2):
            front = max(slots1[i][0], slots2[j][0])
            back = min(slots1[i][1], slots2[j][1])
            if back - front >= duration:
                return [front, front + duration]
            elif slots1[i][1] < slots2[j][1]:
                # if slots1 ended earlier
                i += 1
            else:
                j += 1

        return []


instance = Solution()
s1 = [[10, 50], [60, 120], [140, 210]]
s2 = [[0, 15], [60, 70]]
dur = 12

answer = instance.meetingScheduler(s1, s2, dur)
print answer
