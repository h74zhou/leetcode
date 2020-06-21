class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer = []
        candidates.sort()

        def backtrack(currArr, currSum, start):
            if currSum == target:
                answer.append(currArr)
            else:
                for i in range(start, len(candidates)):
                    if currSum + candidates[i] > target:
                        break
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    currArr.append(candidates[i])
                    backtrack(currArr[:], currSum + candidates[i], i + 1)
                    currArr.pop()

        backtrack([], 0, 0)
        return answer
