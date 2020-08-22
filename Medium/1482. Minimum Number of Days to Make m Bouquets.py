class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def feasible(limit):
            temp = []
            for i in range(len(bloomDay)):
                if bloomDay[i] <= limit:
                    temp.append('x')
                else:
                    temp.append(bloomDay[i])
            answer, count = 0, 0
            for i in range(len(temp)):
                if temp[i] == 'x':
                    count += 1
                    if count == k:
                        answer += 1
                        count = 0
                else:
                    count = 0
            return True if answer >= m else False

        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        if left == max(bloomDay) and not feasible(left):
            return -1

        return left
