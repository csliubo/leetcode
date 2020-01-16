# -*- coding:utf-8 -*-
import copy

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse(self, head, end):
        cur = head
        prev = None
        while prev != end:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        cur = head
        count = 0
        last = None
        while cur:
            count += 1
            if count % k == 0:
                tmp = cur
                if last:
                    last.next.next, last.next, last = tmp.next, self.reverse(last.next, tmp), last.next
                else:
                    last, head.next, head = head, tmp.next, self.reverse(head, tmp)
                cur = last
            cur = cur.next
        return head

    def to_list(self, head):
        tmp = head
        lst = []
        while tmp != None:
            lst.append(tmp.val)
            tmp = tmp.next
        return lst


if __name__ == "__main__":
    head = None
    tmp = None
    for i in range(0, 10):
        if not head:
            head = ListNode(i)
            tmp = head
        else:
            tmp.next = ListNode(i)
            tmp = tmp.next

    tmp = head
    # while tmp != None:
    #     print(tmp.val)
    #     tmp = tmp.next

    s = Solution()
    tmp = s.reverseKGroup(head, 3)
    print(s.to_list(tmp))
    # print(tmp.val)
    while tmp != None:
        print(tmp.val)
        tmp = tmp.next
