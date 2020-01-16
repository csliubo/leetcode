# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "val %s" % (self.val)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tail = None

        def reverse(node):
            if node.next:
                previous = reverse(node.next)
                previous.next = node
                node.next = None
            else:
                nonlocal tail
                tail = node
            return node

        reverse(head)

        return tail


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur is not None:
            print(cur)
            # cur, prev, cur.next = cur.next, cur, prev
            # prev, cur.next, cur = cur, prev, cur.next
            # tmp = cur.next
            # prev = cur
            # cur.next = prev
            # cur = tmp

            a = cur.next
            b = cur
            c = prev
            cur = a
            prev = b
            cur.next = c

            # a = cur
            # b = prev
            # c = cur.next
            # prev = a
            # cur.next = b
            # cur = c

            # prev = cur
            # prev.next = tmp
            # cur = cur.next

            # cur = prev

            # print( cur, prev, cur.next)

        return prev


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
    while tmp != None:
        print(tmp.val)
        tmp = tmp.next

    s = Solution2()
    tmp = s.reverseList(head)
    # print(tmp.val)
    while tmp != None:
        print(tmp.val)
        tmp = tmp.next
