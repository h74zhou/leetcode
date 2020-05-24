class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        length = len(nums)
        
        def backtrack(currArr, currRem, setArray):
            if len(currArr) == length:
                answer.append(currArr)
            else:
                for i in range(len(currRem)):
                    if currRem[i] in setArray:
                        continue
                    currArr.append(currRem[i])
                    setArray.add(currRem[i])
                    tempRem = currRem[:]
                    tempRem.remove(currRem[i])
                    backtrack(currArr[:], tempRem[:], setArray.copy())
                    currArr.pop()
                    setArray.remove(currRem[i])

        arraySet = set()
        backtrack([], nums[:], arraySet)
        return answer
