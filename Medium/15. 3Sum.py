class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return []
        nums.sort()
        answer = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j - 1] == nums[j] and j < k:
                        j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1

        return answer
