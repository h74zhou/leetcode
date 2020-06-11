# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        firstSeq = []
        secondSeq = []

        def dfs(root, t):
            if not root.left and not root.right:
                if t == 1:
                    firstSeq.append(root.val)
                elif t == 2:
                    secondSeq.append(root.val)
            elif not root.left:
                dfs(root.right, t)
            elif not root.right:
                dfs(root.left, t)
            else:
                dfs(root.left, t)
                dfs(root.right, t)

        dfs(root1, 1)
        dfs(root2, 2)
        print firstSeq
        print secondSeq
        return firstSeq == secondSeq
