# -*- coding:utf-8 -*-
from utils import to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if m == n:
            return head
        cur = head
        prev = None
        for i in range(0, m - 1):
            prev, cur = cur, cur.next
        prev_m = prev
        node_m = cur
        for i in range(0, n - m):
            prev, cur.next, cur = cur, prev, cur.next
        if cur:
            prev, cur.next, cur = cur, prev, cur.next
            node_m.next = cur
        if prev_m:
            prev_m.next = prev
        if m == 1:
            return prev
        return head


if __name__ == "__main__":
    head = None
    tmp = None
    for i in range(1, 3):
        if not head:
            head = ListNode(i)
            tmp = head
        else:
            tmp.next = ListNode(i)
            tmp = tmp.next

    tmp = head
    print(to_list(head))

    s = Solution()
    tmp = s.reverseBetween(head, 1, 2)
    # print(tmp.val)
    print(to_list(tmp))
