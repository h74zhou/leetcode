# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.rangeSum = 0

        def recurse(node):
            if not node:
                return 0
            elif node.val > R:
                recurse(node.left)
            elif node.val < L:
                recurse(node.right)
            else:
                self.rangeSum += node.val
                recurse(node.left)
                recurse(node.right)

        recurse(root)
        return self.rangeSum
