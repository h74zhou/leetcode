# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            return max(left, right) + 1

        return depth(root)
