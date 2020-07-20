# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inOrderMap = {}
        for index, value in enumerate(inorder):
            inOrderMap[value] = index

        def inOrderRecurse(preOrder, inStartIndex, inEndIndex):
            if inStartIndex <= inEndIndex:
                rootIndex = inOrderMap[preOrder.pop()]
                newRoot = TreeNode(inorder[rootIndex])
                newRoot.right = inOrderRecurse(preOrder, rootIndex + 1, inEndIndex)
                newRoot.left = inOrderRecurse(preOrder, inStartIndex, rootIndex - 1)
                return newRoot

        return inOrderRecurse(postorder, 0, len(inorder) - 1)
