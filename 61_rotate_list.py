# -*- coding:utf-8 -*-
from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        连成环，然后计算开始位置-1的地方把环断开
        :param head:
        :param k:
        :return:
        '''
        if not head:
            return head
        if not head.next:
            return head

        node_count = 0
        prev, cur = None, head
        while cur:
            node_count += 1
            prev, cur = cur, cur.next
        prev.next = head
        step = node_count - k % node_count
        prev, cur = None, head
        while step:
            prev, cur = cur, cur.next
            step -= 1
        prev.next = None
        return cur


if __name__ == "__main__":
    s = Solution()
    l1 = to_node_list([1, 2, 3, 4, 2, 1])
    print(to_list(s.rotateRight(l1, 3)))
    l1 = to_node_list([1,2,3,4,5])
    print(to_list(s.rotateRight(l1, 3)))
    l1 = to_node_list([1, 2, 3, 4, 5])
    print(to_list(s.rotateRight(l1, 2)))
    l1 = to_node_list([0,1,2])
    print(to_list(s.rotateRight(l1, 4)))