class Solution:
    def copyRandomList(self, head):

        mp = {None: None}
        cur = head

        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            mp[cur].next = mp[cur.next]
            mp[cur].random = mp[cur.random]
            cur = cur.next
            
        return mp[head]