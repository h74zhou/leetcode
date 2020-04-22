public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}

func reverseList(_ head: ListNode?) -> ListNode? {
    var currentNode = head
    var previousNode: ListNode?
    var nextNode: ListNode?
    
    while currentNode != nil {
        nextNode = currentNode?.next
        currentNode?.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    }
    return previousNode
}


