# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, currVal):
            if not node:
                return 0
            elif not node.left and not node.right:
                return currVal * 10 + node.val
            else:
                return dfs(node.left, currVal * 10 + node.val) + dfs(node.right, currVal * 10 + node.val)

        return dfs(root, 0)
