class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        nums.sort()

        if len(nums) == 0:
            return []

        def backtrack(currArr, used):
            if len(currArr) == len(nums):
                answer.append(currArr)
            else:
                for i in range(len(nums)):
                    if used[i]:
                        continue
                    if i > 0 and (nums[i] == nums[i - 1]) and (not used[i - 1]):
                        continue
                    used[i] = True
                    currArr.append(nums[i])
                    backtrack(currArr[:], used[:])
                    currArr.pop()
                    used[i] = False

        used = [False] * len(nums)
        backtrack([], used[:])
        return answer
