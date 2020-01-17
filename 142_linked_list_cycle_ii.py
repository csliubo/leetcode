# -*- coding:utf-8 -*-
from utils import ListNode

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        cache = set()
        cur = head
        while cur:
            if cur in cache:
                return cur
            else:
                cache.add(cur)
                cur = cur.next
        return None
