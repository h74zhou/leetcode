class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        answer = []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(currArr, currIndex):
            if len(currArr) == len(digits):
                if len(currArr) != 0:
                    answer.append(currArr)
            else:
                for letter in phone[digits[currIndex]]:
                    backtrack(currArr + letter, currIndex + 1)

        backtrack("", 0)
        return answer
