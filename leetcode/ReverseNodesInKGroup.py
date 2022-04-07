# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        ptr = head
        count = 1
        prevPtr = ListNode(0, head)
        res = prevPtr
        endPtr = head
        tmpPtr = None
        tmpEndPtr = None
        while endPtr != None:
            count += 1
            endPtr = endPtr.next

            if count == k + 1:
                count = 1
                tmpEndPtr = ptr.next

                while ptr.next != endPtr:
                    tmpPtr = endPtr
                    ptr.next = tmpEndPtr
                    tmpEndPtr = ptr
                    ptr = tmpPtr

                tmpPtr = prevPtr.next
                prevPtr.next = ptr
                ptr.next = tmpEndPtr
                prevPtr = tmpPtr
                ptr = endPtr
        
        return res.next
