class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        answer = []
        answer.append([1])

        for i in range(1, numRows):
            temp = []
            temp.append(1)
            for j in range(1, i):
                prevLeft = answer[i - 1][j - 1]
                prevRight = answer[i - 1][j]
                temp.append(prevLeft + prevRight)
            temp.append(1)
            answer.append(temp)

        return answer
