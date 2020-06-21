class Solution(object):
def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    answer = []
    length = len(nums)
    
    def backtrack(currArr, currIndex):
        answer.append(currArr)
        for i in range(currIndex, length):
            currArr.append(nums[i])
            backtrack(currArr[:], i + 1)
            currArr.pop()
    
    backtrack([], 0)
    return answer
