class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        answer = []

        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        for i in range(len(even)):
            answer.append(even[i])
            answer.append(odd[i])

        return answer
