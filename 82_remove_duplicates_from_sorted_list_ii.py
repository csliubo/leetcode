# -*- coding:utf-8 -*-
from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev, cur, new_head = None, head, None
        while cur:
            duplicated = False
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
                duplicated = True
            if not duplicated:

                if not prev:
                    new_head = cur
                    prev = cur
                else:
                    prev.next = cur
                    prev = prev.next
            else:
                if not cur.next and prev:
                    prev.next = None
            cur = cur.next

        return new_head


if __name__ == "__main__":
    s = Solution()
    l1 = to_node_list([1, 2, 3, 3, 4, 4, 5])
    print(to_list(s.deleteDuplicates(l1)))
    l1 = to_node_list([1, 1, 1, 2, 3])
    print(to_list(s.deleteDuplicates(l1)))
    l1 = to_node_list([1, 1, 1, 2, 3])
    print(to_list(s.deleteDuplicates(l1)))
    l1 = to_node_list([1, 1, 1, 2, 2])
    print(to_list(s.deleteDuplicates(l1)))
    l1 = to_node_list([1, 1, 1])
    print(to_list(s.deleteDuplicates(l1)))
    l1 = to_node_list([])
    print(to_list(s.deleteDuplicates(l1)))
    l1 = to_node_list([8, 9, 9, 11, 12, 13, 13, 14])
    print(to_list(s.deleteDuplicates(l1)))
    l1 = to_node_list([1, 2, 2])
    print(to_list(s.deleteDuplicates(l1)))
