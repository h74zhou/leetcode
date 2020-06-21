class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        answer = []

        def backtrack(currArr, currSum, start):
            if currSum == target:
                answer.append(currArr)
            else:
                for i in range(start, len(candidates)):
                    if currSum + candidates[i] > target:
                        break
                    currArr.append(candidates[i])
                    currSum += candidates[i]
                    backtrack(currArr[:], currSum, i)
                    currArr.pop()
                    currSum -= candidates[i]

        backtrack([], 0, 0)
        return answer
