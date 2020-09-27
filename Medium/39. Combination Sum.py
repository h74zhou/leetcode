class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer = []
        candidates.sort()

        def backtrack(currArr, currSum, currIndex):
            if currSum == target:
                answer.append(currArr[:])
            elif currSum > target:
                return
            else:
                for i in range(currIndex, len(candidates)):
                    backtrack(currArr + [candidates[i]], currSum + candidates[i], i)

        backtrack([], 0, 0)
        return answer
