# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.toList(self.toNumber(l1) + self.toNumber(l2))

    def toNumber(self, l):
        p = l
        total = l.val
        i = 10
        while p.next:
            p = p.next
            total = total + p.val * i
            i *= 10
        return total

    def toList(self, num):
        if num == 0:
            return ListNode(0)
        lst = []
        while num > 0:
            lst.append(num % 10)
            num /= 10
        head = ListNode(lst[0])
        cur = head
        for i in range(1, lst.__len__(), 1):
            cur.next = ListNode(lst[i])
            cur = cur.next
        return head

    def printList(self, l):

        lst = []
        lst.append(str(l.val))
        cur = l
        while cur.next:
            cur = cur.next
            lst.append(str(cur.val))
        print "->".join(lst)


s = Solution()
l1 = s.toList(5)

# l1.next.next = ListNode(3)

# print l1.next.next

# print s.toNumber(l1)

l2 = s.toList(5)
# print s.toNumber(l2)
print s.printList(l1)
print s.printList(l2)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# print s.toNumber(l1)
# print s.toNumber(l2)
#
# print s.toList(0)
# print s.toList(1)
# print s.toList(11)
# print s.toList(12345)
s.printList(s.addTwoNumbers(l1, l2))
