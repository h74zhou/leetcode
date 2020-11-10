class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # bucket[i] represents words with freq of i
        bucket = [None for x in range(len(words) + 1)]
        freq, answer = {}, []

        # create freq {word: freq}
        for word in words:
            freq[word] = freq.get(word, 0) + 1

        # builds the bucket
        for word, freq in freq.iteritems():
            if bucket[freq] is None:
                bucket[freq] = [word]
            else:
                bucket[freq].append(word)

        # sort each individual bucket alphabetically
        for b in bucket:
            if b is not None:
                b.sort()

        curr, count = len(bucket) - 1, 0
        while curr >= 0 and count < k:
            if bucket[curr] is not None:
                for word in bucket[curr]:
                    answer.append(word)
                    count += 1
                    if count >= k:
                        break
            curr -= 1

        return answer
