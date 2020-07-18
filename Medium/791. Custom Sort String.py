class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        answer, tMap = "", {}
        for letter in T:
            if letter in tMap:
                tMap[letter] += 1
            else:
                tMap[letter] = 1

        for letter in S:
            if letter in tMap:
                freq = tMap[letter]
                for i in range(freq):
                    answer += letter
                tMap.pop(letter, 'None')

        for letter, freq in tMap.iteritems():
            for i in range(freq):
                answer += letter

        return answer
