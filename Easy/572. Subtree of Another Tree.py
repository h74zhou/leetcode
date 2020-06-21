# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isEqual(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            elif t1.val != t2.val:
                return False
            elif t1.val == t2.val:
                return isEqual(t1.left, t2.left) and isEqual(t1.right, t2.right)

        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            queue = [s]
            while queue:
                temp = []
                for node in queue:
                    if isEqual(node, t):
                        return True
                    else:
                        if node.left:
                            temp.append(node.left)
                        if node.right:
                            temp.append(node.right)
                queue = temp[:]

            return False
