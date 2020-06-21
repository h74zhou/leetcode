# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def convertListToNum(l):
            arr = []
            while l is not None:
                arr.append(l.val)
                l = l.next
            total = 0
            arr.reverse()
            for i in arr:
                total = 10 * total + i
            return total

        def convertArrtoList(nums):
            if len(nums) == 0:
                return ListNode()
            else:
                currNode = ListNode()
                head = currNode
                for i in range(len(nums)):
                    newNode = ListNode(nums[i])
                    currNode.next = newNode
                    currNode = currNode.next
                return head.next

        newSum = convertListToNum(l1) + convertListToNum(l2)
        newArr = [int(i) for i in str(newSum)]
        newArr.reverse()
        return convertArrtoList(newArr[:])
