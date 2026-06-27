# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        L,p = 0,head
        while p: L,p = L+1,p.next
        dummy = prevtail = ListNode(0,head)
        for _ in range(L//k):
            grouptail = prevtail
            for _ in range(k): grouptail = grouptail.next
            curr,prev,N = prevtail.next,grouptail.next,grouptail.next
            while curr != N: curr.next,prev,curr = prev,curr,curr.next
            prevtail.next,prevtail = grouptail,prevtail.next
        return dummy.next