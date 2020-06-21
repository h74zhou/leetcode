# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.answer = 0

        def dfs(root, currMax):
            if root is None:
                return
            elif root.val >= currMax:
                self.answer += 1
                dfs(root.left, root.val)
                dfs(root.right, root.val)
            elif root.val < currMax:
                dfs(root.left, currMax)
                dfs(root.right, currMax)

        dfs(root, float('-inf'))
        return self.answer
