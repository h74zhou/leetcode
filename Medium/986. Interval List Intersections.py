class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = []
        defaultError = [float('-inf'), float('-inf')]

        def getIntersection(arr1, arr2):
            front = max(arr1[0], arr2[0])
            back = min(arr1[1], arr2[1])
            if back - front >= 0:
                return [front, back]
            return defaultError

        for arrA in A:
            for arrB in B:
                intersection = getIntersection(arrA, arrB)
                if intersection != defaultError:
                    answer.append(intersection)

        return answer
