class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        answer = []
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                answer.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                answer.append(nums2[j])
                j += 1
            else:
                answer.append(nums1[i])
                answer.append(nums2[j])
                i += 1
                j += 1
            # print(answer)

        while i < m:
            answer.append(nums1[i])
            i += 1
            # print(answer)

        while j < n:
            answer.append(nums2[j])
            j += 1
            # print(answer)

        for i in range(len(answer)):
            nums1[i] = answer[i]
