# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        L,p = 0,head
        while p: L,p = L+1,p.next
        dummy = p = ListNode(0,head)
        for _ in range(L//k):
            g = p
            for _ in range(k): g = g.next
            curr,prev,nextstart = p.next,g.next,g.next
            while curr!=nextstart: curr.next,prev,curr = prev,curr,curr.next
            p.next,p = g,p.next
        return dummy.next