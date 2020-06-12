# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.answer = 0

        def dfs(root, parent, gParent):
            if root is None:
                return
            else:
                if gParent and gParent.val % 2 == 0:
                    self.answer += root.val
                dfs(root.left, root, parent)
                dfs(root.right, root, parent)

        dfs(root, None, None)
        return self.answer
