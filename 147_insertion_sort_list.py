# -*- coding:utf-8 -*-
from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tail = head
        while tail.next:
            ele = tail.next
            tail.next = ele.next
            prev, cur = None, head
            if ele.val >= tail.val:
                ele.next = tail.next
                tail.next = ele
                tail = ele
                continue
            if ele.val < head.val:
                ele.next = head
                head = ele
                continue
            while cur != tail.next:
                if ele.val < cur.val:
                    ele.next = cur
                    prev.next = ele
                    break
                else:
                    prev, cur = cur, cur.next
        return head


if __name__ == "__main__":
    s = Solution()
    l1 = to_node_list([])
    print(to_list(s.insertionSortList(l1)))

    l1 = to_node_list([1, 2, 3])
    print(to_list(s.insertionSortList(l1)))
    l1 = to_node_list([3, 2, 1])
    print(to_list(s.insertionSortList(l1)))
    l1 = to_node_list([3])
    print(to_list(s.insertionSortList(l1)))
    l1 = to_node_list([3, 2, 1, 4])
    print(to_list(s.insertionSortList(l1)))
    l1 = to_node_list([3, 2, 1, 4, 5, 9, 8])
    print(to_list(s.insertionSortList(l1)))
    l1 = to_node_list([3, 2, 1, 4, 5, 9, 8, 8])
    print(to_list(s.insertionSortList(l1)))
    l1 = to_node_list([0, 0, 0])
    print(to_list(s.insertionSortList(l1)))
    l1 = to_node_list([0, -1, -1])
    print(to_list(s.insertionSortList(l1)))
    l1 = to_node_list([])
    print(to_list(s.insertionSortList(l1)))
