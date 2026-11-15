# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        t = ListNode(0,head)
        c = t
        p = t

        for _ in range(n):
            c = c.next
        
        while c.next:
            c = c.next
            p = p.next
        p.next = p.next.next
        
        return t.next
        