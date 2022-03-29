import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # hqueue = []
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        pq = []
        for l in lists:
            heapq.heappush(pq, l)
        res = ListNode(None)
        head = res
        while pq:
            l = heapq.heappop(pq)
            head.next = l
            head = head.next
            if l.next:
                heapq.heappush(pq, l.next)
        return res


