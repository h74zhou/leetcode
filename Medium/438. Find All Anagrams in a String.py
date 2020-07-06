class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []

        arr1 = [0] * 26
        for letter in p:
            arr1[ord(letter) - 97] += 1

        start, end, arr2, answer = 0, len(p) - 1, [0] * 26, []

        for i in range(end + 1):
            print ord(s[i]), s[i], i
            arr2[ord(s[i]) - 97] += 1

        while end < len(s):
            if arr1 == arr2:
                answer.append(start)
            if end + 1 >= len(s):
                break

            arr2[ord(s[start]) - 97] -= 1
            start += 1
            end += 1
            arr2[ord(s[end]) - 97] += 1

        return answer
