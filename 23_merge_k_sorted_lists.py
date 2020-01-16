# -*- coding:utf-8 -*-
import copy
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        '''
        暴力解法，应该不符合出题者的意图
        :param lists:
        :return:
        '''
        nums = []
        for i in range(0, len(lists)):
            if lists[i]:
                tmp = lists[i]
                while tmp != None:
                    nums.append(tmp.val)
                    tmp = tmp.next

        head, cur = None, None
        for num in sorted(nums):
            if not head:
                cur = head = ListNode(num)
            else:
                cur.next = ListNode(num)
                cur = cur.next
        return head

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        :param lists:
        :return:
        '''
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        tmp_lists = [l for l in lists]

        while len(tmp_lists) > 1:
            tmp = []
            for i in range(0, len(tmp_lists) - 1, 2):
                tmp.append(self.merge2Lists(tmp_lists[i], tmp_lists[i + 1]))
            if len(tmp_lists) % 2 != 0:
                tmp.append(tmp_lists[-1])
            tmp_lists = tmp
        return tmp_lists[0]

    def merge2Lists(self, lst_a, lst_b) -> ListNode:
        '''
        合并两个链表
        :param lists:
        :return:
        '''
        if lst_a and not lst_b:
            return lst_a
        if lst_b and not lst_a:
            return lst_b
        p_a, p_b = lst_a, lst_b
        head = None
        if p_a.val < p_b.val:
            head = p_a
            p_a = p_a.next
        else:
            head = p_b
            p_b = p_b.next
        cur = head
        while p_a and p_b:
            if p_a.val > p_b.val:
                cur.next = p_b
                p_b = p_b.next
            else:
                cur.next = p_a
                p_a = p_a.next
            cur = cur.next
        if p_a:
            cur.next = p_a
        else:
            cur.next = p_b
        return head

    def to_list(self, head):
        tmp = head
        lst = []
        while tmp != None:
            lst.append(tmp.val)
            tmp = tmp.next
        return lst


if __name__ == "__main__":

    for i in range(0, 3 - 1, 2):
        print(i, i + 1)
    # exit(0)
    head = None
    tmp = None
    for i in range(0, 10):
        if not head:
            head = ListNode(i)
            tmp = head
        else:
            tmp.next = ListNode(i)
            tmp = tmp.next
    lst = [head]
    h2 = None
    for i in range(0, 4):
        if not h2:
            h2 = ListNode(i)
            tmp = h2
        else:
            tmp.next = ListNode(i)
            tmp = tmp.next
    lst.append(h2)
    h3 = None
    for i in range(0, 4):
        if not h3:
            h3 = ListNode(i)
            tmp = h3
        else:
            tmp.next = ListNode(i)
            tmp = tmp.next
    lst.append(h3)

    s = Solution()
    print(s.to_list(s.mergeKLists(lst)))
