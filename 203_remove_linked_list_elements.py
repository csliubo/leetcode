# -*- coding:utf-8 -*-
from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        prev, cur = None, head
        while cur:
            if cur.val == val:
                if not prev:
                    head, cur = cur.next, cur.next
                else:
                    prev.next, cur = cur.next, cur.next
            else:
                prev, cur = cur, cur.next
        return head


if __name__ == "__main__":
    l1 = to_node_list([8, 4, 3, 2, 5, 2])

    s = Solution()
    print(to_list(s.removeElements(l1, 3)))
    l1 = to_node_list([])
    print(to_list(s.removeElements(l1, 3)))

    l1 = to_node_list([3, 2, 5, 4])
    print(to_list(s.removeElements(l1, 3)))

    l1 = to_node_list([3])
    print(to_list(s.removeElements(l1, 3)))
    l1 = to_node_list([0])
    print(to_list(s.removeElements(l1, 3)))
