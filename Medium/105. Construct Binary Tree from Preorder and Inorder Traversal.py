# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inOrderMap = {}
        for index, value in enumerate(inorder):
            inOrderMap[value] = index

        def inOrderRecurse(preOrder, inStartIndex, inEndIndex):
            if inStartIndex <= inEndIndex:
                rootIndex = inOrderMap[preOrder.pop(0)]
                newRoot = TreeNode(inorder[rootIndex])
                newRoot.left = inOrderRecurse(preOrder, inStartIndex, rootIndex - 1)
                newRoot.right = inOrderRecurse(preOrder, rootIndex + 1, inEndIndex)
                return newRoot

        return inOrderRecurse(preorder, 0, len(inorder) - 1)
