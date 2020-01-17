# -*- coding:utf-8 -*-
from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def isPalindrome1(self, head: ListNode) -> bool:
        if not head:
            return False
        cur = head
        if not head.next:
            return True
        lst = []
        while cur:
            lst.append(cur.val)
            cur = cur.next
        half_size = int(len(lst) / 2)
        for i in range(0, half_size):
            if lst[i] != lst.pop():
                return False
        return True

    def isPalindrome(self, head: ListNode) -> bool:
        '''
        解法2，可以计算中间位置，然后从中间位置开始反转链表，然后比较开头到中间和中间到结尾
        :param head:
        :return:
        '''
        if not head:
            return False
        cur = head
        if not head.next:
            return True
        lst = []
        while cur:
            lst.append(cur.val)
            cur = cur.next
        half_size = int(len(lst) / 2)
        for i in range(0, half_size):
            if lst[i] != lst.pop():
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    l1 = to_node_list([1, 2, 3, 3, 2, 1])
    print(s.isPalindrome(l1))
    l1 = to_node_list([1, 1])
    print(s.isPalindrome(l1))
    l1 = to_node_list([1])
    print(s.isPalindrome(l1))
    l1 = to_node_list([1, 2])
    print(s.isPalindrome(l1))
    l1 = to_node_list([1, 2, 3, 2, 1])
    print(s.isPalindrome(l1))
