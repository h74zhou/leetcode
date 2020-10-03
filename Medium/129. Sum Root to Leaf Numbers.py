# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        def dfs(currStr, currNode):
            if not currNode.left and not currNode.right:
                val = int(currStr + str(currNode.val))
                self.total += val
            elif not currNode.left:
                self.total += int(currStr) if len(currStr) > 0 else 0
                dfs(currStr + str(currNode.val), currNode.right)
            elif not currNode.right:
                self.total += int(currStr) if len(currStr) > 0 else 0
                dfs(currStr + str(currNode.val), currNode.left)
            else:
                dfs(currStr + str(currNode.val), currNode.left)
                dfs(currStr + str(currNode.val), currNode.right)

        if not root:
            return 0

        dfs("", root)
        return self.total
