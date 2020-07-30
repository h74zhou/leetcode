class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        hash = [0 for x in range(26)]
        mostFreqLetter, mostFreq = "", 0
        for c in S:
            hash[ord(c) - 97] += 1
            if hash[ord(c) - 97] > mostFreq:
                mostFreq = hash[ord(c) - 97]
                mostFreqLetter = c

        if mostFreq > (len(S) + 1) / 2:
            return ""
        index, ansArr = 0, ["?" for x in range(len(S))]

        while hash[ord(mostFreqLetter) - 97] > 0:
            ansArr[index] = mostFreqLetter
            hash[ord(mostFreqLetter) - 97] -= 1
            index += 2

        for i in range(len(hash)):
            while hash[i] > 0:
                if index >= len(S):
                    index = 1
                ansArr[index] = chr(i + 97)
                index += 2
                hash[i] -= 1

        return ''.join(ansArr)
