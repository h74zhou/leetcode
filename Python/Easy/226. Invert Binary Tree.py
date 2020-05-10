# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        elif root.left is None and root.right is None:
            return root
        elif root.left is None or root.right is None:
            if root.left is None:
                root.left = root.right
                root.right = None
            else:
                root.right = root.left
                root.left = None
            self.invertTree(root.left)
            self.invertTree(root.right)
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
