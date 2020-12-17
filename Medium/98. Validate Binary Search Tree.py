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
        def helper(node, leftVal, rightVal):
            if node is None:
                return True
            if leftVal >= node.val or rightVal <= node.val:
                return False
            if not helper(node.left, leftVal, node.val):
                return False
            if not helper(node.right, node.val, rightVal):
                return False
            return True

        return helper(root, float('-inf'), float('inf'))

