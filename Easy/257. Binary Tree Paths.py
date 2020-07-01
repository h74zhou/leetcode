# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        answer = []

        def dfs(node, currStr):
            if not node.left and not node.right:
                answer.append(currStr + str(node.val))
            else:
                if node.left:
                    dfs(node.left, currStr + str(node.val) + "->")
                if node.right:
                    dfs(node.right, currStr + str(node.val) + "->")

        if root is None:
            return []

        dfs(root, "")
        return answer
