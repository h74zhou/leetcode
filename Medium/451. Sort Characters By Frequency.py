class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        bucket = [None for x in range(len(s) + 1)]
        freq, answer = {}, ""

        # creates freq mapping of letter: freq
        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1

        for letter, freq in freq.iteritems():
            if bucket[freq] is None:
                bucket[freq] = [letter]
            else:
                bucket[freq].append(letter)

        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i] is not None:
                for letter in bucket[i]:
                    answer += i * letter

        return answer
