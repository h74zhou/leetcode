import sys


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left, right, count = 0, len(people) - 1, 0

        while left <= right:
            if left == right:
                return count + 1
            elif people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            count += 1

        return count


instance = Solution()
print instance.numRescueBoats([1, 2], 3)
