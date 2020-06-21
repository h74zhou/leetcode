class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i = 0
        k = len(nums) - 1

        if len(nums) < 3:
            return []

        answer = []

        # N iterations
        for i in range(0, len(nums)):
            # Bounded by N
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            # Bounded by N
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1

        return answer
