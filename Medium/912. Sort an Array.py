class Solution(object):
    def merge(self, left, right):
        answer = []
        l, r = 0, 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                answer.append(left[l])
                l += 1
            else:
                answer.append(right[r])
                r += 1

        while l < len(left):
            answer.append(left[l])
            l += 1

        while r < len(right):
            answer.append(right[r])
            r += 1

        return answer

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        left = self.sortArray(nums[:len(nums) / 2])
        right = self.sortArray(nums[len(nums) / 2:])
        return merge(left, right)
