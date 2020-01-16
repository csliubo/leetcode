# -*- coding:utf-8 -*-
from utils import to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        prev, new_head = None, None
        nodes_map = {}
        while cur:
            new_node = Node(cur.val, random=cur.random)
            nodes_map[cur] = new_node
            if not new_head:
                new_head = new_node
                prev = new_head
            else:
                prev.next = new_node
                cur, prev = cur.next, prev.next
        cur = new_head
        while cur:
            if cur.random:
                cur.random = nodes_map.get(cur.random)
        return new_head


if __name__ == "__main__":
    l1 = to_node_list([8, 4, 3, 2, 5, 2])

    s = Solution()
    print(to_list(s.copyRandomList(l1)))
    l1 = to_node_list([])
    print(to_list(s.copyRandomList(l1)))
