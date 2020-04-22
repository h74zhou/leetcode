public class ListNode {
    public var val : Int
    public var next : ListNode?
    public init(_val: Int) {
        self.val - val
        self.next = nil
    }
}

func mergeTwoLists(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
    var head : ListNode
    var current = head
    
    while true {
        if l1 == nil || l2 == nil {
            break
        }
        
        if l1!.val <= l2!.val {
            current.next = l1
            current = l1!
            l1 = l1!.next
        } else {
            current.next = l2
            current = l2
            l2 = l2.next
        }
    }
    
    if l1 == nil {
        while l2 != nil {
            current.next = l2
            current = l2
            l2 = l2.next
        }
    }
    
    if l2 == nil {
        while l1 != nil {
            current.next = l1
            current = l1
            l1 = l1.next
        }
    }
    return head.next
}
