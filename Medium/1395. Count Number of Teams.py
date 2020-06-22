class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """

        count = 0
        for i in range(len(rating)):
            for j in range(1, len(rating)):
                for k in range(2, len(rating)):
                    if 0 <= i < j < k and (rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]):
                        count += 1
        return count
