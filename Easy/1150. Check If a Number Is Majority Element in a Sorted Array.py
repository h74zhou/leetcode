class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, length, right = 0, len(nums), len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return True if nums[left + (length / 2)] == target else False


test1 = [2, 4, 5, 5, 5, 5, 5, 6, 6]
target1 = 5
test2 = [10, 100, 101, 101]
target2 = 101

instance = Solution()
instance.isMajorityElement(test1, target1)
