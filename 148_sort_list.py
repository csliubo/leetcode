# -*- coding:utf-8 -*-
from random import randint

from utils import to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        '''
        两两切分链表，直到链表只剩一条记录，然后两两归并，这样归并时的单个链表都是有序的，总体复杂度时O(nlogn)
        :param head:
        :return:
        '''

        def split(head: ListNode):
            cur = None
            l_head = head
            if not head.next:
                return head
            r_head = head.next
            l_p, r_p = l_head, r_head
            if r_head:
                cur = r_head.next
            while cur:
                l_p.next, r_p.next = cur, cur.next
                l_p, r_p = l_p.next, r_p.next
                cur = cur.next
                if cur and cur.next:
                    cur = cur.next
                else:
                    break
            if l_p:
                l_p.next = None
            if r_p:
                r_p.next = None
            return l_head, r_head

        def merge(l1: ListNode, l2: ListNode):
            cur, head = None, None
            p1, p2 = l1, l2
            if l1 and not l2:
                return l1
            if l2 and not l1:
                return l2
            if l1.val < l2.val:
                head, cur, p1 = l1, l1, l1.next
            else:
                head, cur, p2 = l2, l2, l2.next
            while p1 and p2:
                if p1.val < p2.val:
                    cur.next, cur, p1 = p1, p1, p1.next
                else:
                    cur.next, cur, p2 = p2, p2, p2.next
            if p1:
                cur.next = p1
            if p2:
                cur.next = p2
            return head

        def split_and_merge(head: ListNode):
            l, r = split(head)
            if not r:
                return l
            if l.next:
                l = split_and_merge(l)
            if r.next:
                r = split_and_merge(r)

            h = merge(l, r)

            return h

        return split_and_merge(head)


if __name__ == "__main__":
    head = None
    tmp = None
    for i in range(0, 10):
        val = randint(1, 100)
        if not head:
            head = ListNode(val)
            tmp = head
        else:
            tmp.next = ListNode(val)
            tmp = tmp.next
    print(to_list(head))
    s = Solution()
    print(to_list(s.sortList(head)))
