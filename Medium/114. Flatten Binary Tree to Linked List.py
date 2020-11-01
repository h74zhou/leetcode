# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root

        curr = root

        while curr:
            # find the leftMax
            if curr.left:
                leftMax = curr.left
                while leftMax.right:
                    leftMax = leftMax.right

                # connects leftmax to start of the right branch of curr
                leftMax.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
