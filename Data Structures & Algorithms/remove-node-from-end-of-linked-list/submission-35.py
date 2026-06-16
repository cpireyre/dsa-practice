# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = curr = ListNode(0,head)
        for _ in range(n+1): curr = curr.next
        p = dummy
        while curr: curr,p = curr.next,p.next
        p.next = p.next.next
        return dummy.next