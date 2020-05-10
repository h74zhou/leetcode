class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = [1, i]
            else:
                map[s[i]][0] += 1

        answer = float('inf')
        for key, value in map.iteritems():
            # print(key, value)
            if value[0] == 1 and value[1] < answer:
                answer = value[1]

        if answer < float('inf'):
            return answer

        return -1
