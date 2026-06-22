# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(p,q):
    dummy = curr = ListNode()
    while p and q:
        if p.val < q.val: curr.next,p = p,p.next
        else: curr.next,q = q,q.next
        curr = curr.next
    curr.next = p or q
    return dummy.next 

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            merged = [merge(*p) for p in zip(lists[::2],lists[1::2])]
            if len(lists) % 2: merged.append(lists[-1])
            lists = merged
        return lists[0] if lists else None