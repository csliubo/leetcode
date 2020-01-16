# -*- coding:utf-8 -*-
from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        cur = head
        node_lst = []
        while cur:
            node_lst.append(cur)
            cur = cur.next

        node_count = len(node_lst)
        for i in range(0, int(node_count / 2)):
            left_node, right_node = node_lst[i], node_lst[node_count - i - 1]
            if left_node.next != right_node:
                right_node.next, left_node.next = left_node.next, right_node

        node_lst[int(node_count / 2)].next = None
        # print("after")
        # print(to_list(node_lst[0]))
        # head = node_lst[0]

if __name__ == "__main__":
    l1 = to_node_list([7, 2, 4, 3])
    l2 = to_node_list([5, 6, 4])

    s = Solution()
    s.reorderList(l1)
    print(to_list(l1))
    s.reorderList(l2)
    print(to_list(l2))
    l1 = to_node_list([7, 3, 1])
    l2 = to_node_list([0])
    s.reorderList(l1)
    s.reorderList(l2)
    print(to_list(l1))
    print(to_list(l2))
