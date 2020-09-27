class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        answer = []

        def backtrack(currArr, currSum, currNum):
            if currSum == n and len(currArr) == k:
                answer.append(currArr[:])
            elif currSum > n or len(currArr) > k:
                return
            else:
                for i in range(currNum, 10):
                    backtrack(currArr + [i], currSum + i, i + 1)

        backtrack([], 0, 1)
        return answer
