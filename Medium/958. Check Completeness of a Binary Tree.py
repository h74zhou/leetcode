# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        end = False
        queue = [root]

        while queue:
            front = queue.pop(0)
            if not front:
                end = True
            else:
                if end:
                    return False
                queue.append(front.left)
                queue.append(front.right)

        return True
