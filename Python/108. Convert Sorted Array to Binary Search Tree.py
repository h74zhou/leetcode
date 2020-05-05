# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def operate(left, right):
            if left > right:
                return None
            mid = (left + right) / 2
            node = TreeNode()
            node.val = nums[mid]
            node.left = operate(left, mid - 1)
            node.right = operate(mid + 1, right)
            return node

        return operate(0, len(nums) - 1)
