class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        answer = []
        nums = []
        for i in range(1, n + 1):
            nums.append(i)

        def backtrack(currArr, currIndex):
            if len(currArr) == k:
                answer.append(currArr)
            else:
                for i in range(currIndex, len(nums)):
                    currArr.append(nums[i])
                    backtrack(currArr[:], i + 1)
                    currArr.pop()

        backtrack([], 0)
        return answer
