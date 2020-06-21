class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortedStrs = []
        for s in strs:
            sortedStrs.append(''.join(sorted(s)))

        d = {}

        for index, s in enumerate(sortedStrs):
            if s in d:
                d[s] += [index]
            else:
                d[s] = [index]

        answer = []

        for key, value in d.iteritems():
            temp = []
            for index in value:
                temp.append(strs[index])
            answer.append(temp)

        return answer
