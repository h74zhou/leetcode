class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ""

        for word in s.split():
            answer += word[::-1]
            answer += " "
        return answer[:len(answer) - 1]
