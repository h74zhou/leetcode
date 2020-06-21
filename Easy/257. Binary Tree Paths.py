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

        def dfs(root, currStr):
            if not root.left and not root.right:
                answer.append(currStr + "->" + str(root.val))
            else:
                if root.left:
                    dfs(root.left, currStr + "->" + str(root.val))
                if root.right:
                    dfs(root.right, currStr + "->" + str(root.val))

        if root is None:
            return ""

        dfs(root, "")
        for i in range(len(answer)):
            string = answer[i]
            string = string[2:]
            answer[i] = string

        return answer
