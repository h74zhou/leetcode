class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        answer = []

        while i < len(nums1) and j < len(nums2):
            first = nums1[i]
            second = nums2[j]
            if first == second:
                answer.append(first)
                while first == nums1[i]:
                    i += 1
                    if i >= len(nums1):
                        return answer
                while second == nums2[j]:
                    j += 1
                    if j >= len(nums2):
                        return answer
            elif first > second:
                j += 1
            else:
                i += 1

        return answer
