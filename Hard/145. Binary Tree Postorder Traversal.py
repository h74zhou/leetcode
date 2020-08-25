# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            answer.append(node.val)
        traverse(root)
        return answer
