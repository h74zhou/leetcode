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
        self.total = 0

        def dfs(root):
            if root is None:
                return
            if root.val >= L and root.val <= R:
                self.total += root.val
                dfs(root.left)
                dfs(root.right)
            elif root.val >= L:
                dfs(root.left)
            elif root.val <= R:
                dfs(root.right)

        dfs(root)
        return self.total
