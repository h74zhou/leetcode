class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numArr = [int(i) for i in str(num)]
        currMax, currMaxIndex, leftMostMinIndex, lastMaxSwap = float('-inf'), -1, -1, -1

        for i in range(len(numArr) - 1, -1, -1):
            if numArr[i] > currMax:
                currMax = numArr[i]
                currMaxIndex = i
            elif numArr[i] < currMax:
                leftMostMinIndex = i
                lastMaxSwap = currMaxIndex

        if leftMostMinIndex == -1:
            return num

        numArr[lastMaxSwap], numArr[leftMostMinIndex] = numArr[leftMostMinIndex], numArr[lastMaxSwap]
        return int(''.join(map(str, numArr)))
