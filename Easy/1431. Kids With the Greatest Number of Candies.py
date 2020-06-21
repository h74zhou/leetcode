class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandy = max(candies)
        answer = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandy:
                answer.append(True)
            else:
                answer.append(False)

        return answer
