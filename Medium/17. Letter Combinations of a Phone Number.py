class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        answer = []

        def backtrack(currStr, currIndex):
            if len(currStr) == len(digits):
                answer.append(currStr[:])
            else:
                for i in range(currIndex, len(digits)):
                    for letter in d[digits[i]]:
                        backtrack(currStr + letter, i + 1)

        if len(digits) == 0:
            return []

        backtrack("", 0)
        return answer
