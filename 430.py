__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        def flat_current_list(node: Node) -> Node:
            prev, cur = None, node
            while cur:
                if cur.child:
                    first_child_node = cur.child
                    last_child_node = flat_current_list(first_child_node)
                    first_child_node.prev = cur
                    cur_next = cur.next
                    cur.next = first_child_node
                    last_child_node.next = cur_next
                    if cur_next:
                        cur_next.prev = last_child_node
                    prev, cur = last_child_node, cur_next
                else:
                    prev, cur = None, cur.next
            return prev

        return flat_current_list(head)
