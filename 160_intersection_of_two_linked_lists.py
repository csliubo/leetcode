# -*- coding:utf-8 -*-
from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        count_a = 0
        count_b = 0
        cur = headA
        while cur:
            cur = cur.next
            count_a += 1
        cur = headB
        while cur:
            cur = cur.next
            count_b += 1
        cur_a, cur_b = headA, headB
        if count_a > count_b:
            for i in range(0, count_a - count_b):
                cur_a = cur_a.next
        else:
            for i in range(0, count_b - count_a):
                cur_b = cur_b.next
        while cur_a and cur_b:
            if cur_a == cur_b:
                return cur_a
            cur_a, cur_b = cur_a.next, cur_b.next
        return None


if __name__ == "__main__":
    s = Solution()
    l1 = to_node_list([1, 2, 3, 3, 4])
    l2 = to_node_list([1, 2, 3, 4, 5])
    print(to_list(s.getIntersectionNode(l1, l2)))
