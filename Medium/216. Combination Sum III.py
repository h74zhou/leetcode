class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(1, 10):
            nums.append(i)

        answer = []

        def backtrack(currArr, currSum, currIndex):
            if len(currArr) == k and currSum == n:
                answer.append(currArr)
            elif len(currArr) == k and currSum > n:
                return
            elif len(currArr) > k:
                return
            else:
                for i in range(currIndex, 9):
                    currArr.append(nums[i])
                    backtrack(currArr[:], currSum + nums[i], i + 1)
                    currArr.pop()

        backtrack([], 0, 0)
        return answer
