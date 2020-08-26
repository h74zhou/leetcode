# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        if not root:
            return answer

        stack = [root]
        while stack:
            last = stack.pop()
            answer.append(last.val)
            if last.right:
                stack.append(last.right)
            if last.left:
                stack.append(last.left)
        return answer
