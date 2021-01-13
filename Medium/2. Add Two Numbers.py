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
        num1, num2 = "", ""
        node1, node2 = l1, l2

        while node1:
            num1 += str(node1.val)
            node1 = node1.next

        while node2:
            num2 += str(node2.val)
            node2 = node2.next

        num1, num2 = num1[::-1], num2[::-1]
        answer = str(int(num1) + int(num2))

        start = ListNode()
        curr = start

        for i in range(len(answer) - 1, -1, -1):
            letter = answer[i]
            newNode = ListNode(int(letter))
            curr.next = newNode
            curr = curr.next

        return start.next



