class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head : 
            return None
        map = {}
        curr = head

        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            new_node = map[curr]
            new_node.next = map.get(curr.next)
            new_node.random = map.get(curr.random)
            curr = curr.next
        return map[head]

