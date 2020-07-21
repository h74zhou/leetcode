# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        queue = [cloned]

        while queue:
            node = queue.pop()
            if node.val == target.val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
