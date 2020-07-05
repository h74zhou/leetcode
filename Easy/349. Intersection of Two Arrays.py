class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1, d2 = {}, {}

        for num in nums1:
            if num in d1:
                d1[num] += 1
            else:
                d1[num] = 1

        for num in nums2:
            if num in d1:
                d2[num] = 1

        return [n for n in d2]
