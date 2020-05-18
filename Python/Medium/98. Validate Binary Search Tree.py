# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root, left, right):
            if root is None:
                return True

            if root.val <= left or root.val >= right:
                return False

            if not helper(root.left, left, root.val):
                return False

            if not helper(root.right, root.val, right):
                return False

            return True

        return helper(root, float('-inf'), float('inf'))
