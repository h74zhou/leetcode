/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */
class Solution {
    func removeElements(_ head: ListNode?, _ val: Int) -> ListNode? {
        var currentNode = head
        var firstNode = head
        var previousNode : ListNode?
        var nextNode : ListNode?
        
        while currentNode != nil {
            nextNode = currentNode?.next
            if currentNode?.val == val {
                // if it's the first node
                if currentNode?.val == firstNode?.val {
                    firstNode = currentNode?.next
                } else {
                    previousNode?.next = currentNode?.next
                }
            } else {
                previousNode = currentNode
            }
            currentNode = currentNode?.next
        }
        return firstNode
    }
}
