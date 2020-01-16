# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        '''
        解法1，遍历统计数量，算出要删除的位置,然后遍历删除
        :param head:
        :param n:
        :return:
        '''
        cur = head
        prev = None
        if not head:
            return None

        total_count = 0
        while cur:
            cur = cur.next
            total_count += 1

        need_remove_index = total_count - n
        if need_remove_index == 0:
            return head.next
        cur = head
        for i in range(0, need_remove_index):
            prev, cur = cur, cur.next
        prev.next = cur.next
        return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        解法2，遍历统计数量，同时将下表和节点对应缓存起来，算出要删除的位置
        :param head:
        :param n:
        :return:
        '''
        cur = head
        if not head:
            return None

        total_count = 0
        node_map = {}
        while cur:
            node_map[total_count] = cur
            cur = cur.next
            total_count += 1

        need_remove_index = total_count - n
        if need_remove_index == 0:
            return head.next
        else:
            prev_node = node_map[need_remove_index - 1]
            prev_node.next = node_map[need_remove_index].next
        return head
