# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.xParent = None
        self.yParent = None
        self.xLevel = float('inf')
        self.yLevel = float('-inf')

        if not root:
            return False

        def dfs(root, level):
            if not root:
                return
            if self.xLevel != float('inf') and self.yLevel != float('-inf'):
                return
            if root.left and root.left.val == x:
                self.xParent = root
                self.xLevel = level + 1
            elif root.left and root.left.val == y:
                self.yParent = root
                self.yLevel = level + 1
            elif root.right and root.right.val == x:
                self.xParent = root
                self.xLevel = level + 1
            elif root.right and root.right.val == y:
                self.yParent = root
                self.yLevel = level + 1
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return self.xLevel == self.yLevel and self.xParent != self.yParent
