# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val == right.val:
            return True and self.isMirror(left.right, right.left) and self.isMirror(left.left, right.right)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
