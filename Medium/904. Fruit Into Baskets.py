class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        d = {tree[0]: 1}
        start, end, dCount, longest = 0, 0, 1, float('-inf')

        while end < len(tree):
            if dCount <= 2:
                longest = max(longest, end - start + 1)
                end += 1
                if end >= len(tree):
                    continue
                elif tree[end] in d:
                    d[tree[end]] += 1
                else:
                    d[tree[end]] = 1
                    dCount += 1
            else:
                amt = d.get(tree[start])
                if amt <= 1:
                    d.pop(tree[start])
                    dCount -= 1
                else:
                    d[tree[start]] = amt - 1
                start += 1

        return longest


