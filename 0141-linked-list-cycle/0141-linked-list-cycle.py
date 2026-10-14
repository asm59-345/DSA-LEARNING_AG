# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        prev = head
        curr = head

        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next

            if prev == curr:
                return True
        return False