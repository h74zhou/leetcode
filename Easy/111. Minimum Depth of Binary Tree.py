# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        queue = [(root, 1)]

        while queue:
            node, level = queue.pop(0)
            if node:
                if node.left is None and node.right is None:
                    return level
                else:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))

        return 1
