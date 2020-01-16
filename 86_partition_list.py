# -*- coding:utf-8 -*-
from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        node_x, prev_x, cur = None, None, head
        while cur and cur.val < x:
            prev_x, cur = cur, cur.next
        if not cur:
            return head
        node_x = cur
        prev = prev_x
        while cur:
            if cur.val < x:
                # insert x between prev_x and node_x
                prev.next = cur.next
                if not prev_x:
                    head = cur
                    prev_x = cur
                else:
                    prev_x.next = cur
                    prev_x = cur
                cur.next = node_x
            prev, cur = cur, cur.next

        return head


if __name__ == "__main__":
    l1 = to_node_list([8, 4, 3, 2, 5, 2])

    s = Solution()
    print(to_list(s.partition(l1, 3)))
    l1 = to_node_list([])
    print(to_list(s.partition(l1, 3)))

    l1 = to_node_list([3, 2, 5, 4])
    print(to_list(s.partition(l1, 3)))


    l1 = to_node_list([3])
    print(to_list(s.partition(l1, 3)))
    l1 = to_node_list([0])
    print(to_list(s.partition(l1, 3)))

