# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return root

        d = {}
        queue = [root]

        while queue:
            last = queue.pop()
            if k - last.val in d:
                return True
            d[last.val] = 1
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)

        return False
