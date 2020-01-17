# -*- coding:utf-8 -*-
from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        cur = head.next.next
        if not cur:
            return head
        odd_prev, even_prev, even_head = head, head.next, head.next
        while cur:
            if cur.next:
                odd_prev.next, odd_prev = cur, cur
                even_prev.next, even_prev = cur.next, cur.next
                cur = cur.next.next
            else:
                even_prev.next = None
                odd_prev.next, odd_prev = cur, cur
                cur = cur.next
        odd_prev.next = even_head

        return head


if __name__ == "__main__":
    s = Solution()
    l1 = to_node_list([])
    print(to_list(s.oddEvenList(l1)))

    l1 = to_node_list([1, 2, 3])
    print(to_list(s.oddEvenList(l1)))
    l1 = to_node_list([1, 2])
    print(to_list(s.oddEvenList(l1)))
    l1 = to_node_list([1])
    print(to_list(s.oddEvenList(l1)))
    l1 = to_node_list([])
    print(to_list(s.oddEvenList(l1)))
    l1 = to_node_list([1, 2, 3, 4, 5, 6])
    print(to_list(s.oddEvenList(l1)))
