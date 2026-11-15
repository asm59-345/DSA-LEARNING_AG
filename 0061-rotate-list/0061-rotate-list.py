# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
            
        curr.next = head

        k = k % length
        steps_tail = length - k - 1

        new_tail = head
        for _ in range(steps_tail):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None

        return new_head