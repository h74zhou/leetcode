class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        answer = []

        for person, size in enumerate(groupSizes):
            if size == 1:
                answer.append([person])
            elif size in d and len(d[size]) < size:
                d[size].append(person)
                if len(d[size]) >= size:
                    answer.append(d[size])
                    d.pop(size, 'None')
            else:
                d[size] = [person]

        for size, value in d.iteritems():
            answer.append(value)

        return answer
