# -*- coding:utf-8 -*-
from utils import to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getNum(l1: ListNode):
            val, factor = l1.val, 1
            if l1.next:
                ret_val, ret_factor = getNum(l1.next)
                factor += ret_factor
                val = ret_val + l1.val * pow(10, factor - 1)
            return val, factor

        num1, _ = getNum(l1)
        num2, _ = getNum(l2)
        head = None
        tmp = None
        for ch in str(num1 + num2):
            if not head:
                head = ListNode(int(ch))
                tmp = head
            else:
                tmp.next = ListNode(int(ch))
                tmp = tmp.next
        return head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        解法2，类似堆栈，高位先入栈，低位先出栈
        :param l1:
        :param l2:
        :return:
        '''
        s_1 = []
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        while l1:
            s_1.append(l1.val)
            l1 = l1.next
        s_2 = []
        while l2:
            s_2.append(l2.val)
            l2 = l2.next
        carry_bit = False
        sum_digits = []
        short_len = min(len(s_1), len(s_2))

        for i in range(0, short_len):
            val = s_1.pop() + s_2.pop()
            if carry_bit:
                val += 1
            carry_bit = False
            if val >= 10:
                val = val - 10
                carry_bit = True
            sum_digits.append(val)
        long_l = s_1 if len(s_1) > len(s_2) else s_2
        while len(long_l) > 0:
            val = long_l.pop()
            if carry_bit:
                val += 1
            carry_bit = False
            if val >= 10:
                val -= 10
                carry_bit = True
            sum_digits.append(val)
        if carry_bit:
            sum_digits.append(1)
        head = None
        tmp = None
        for i in range(len(sum_digits), 0, -1):
            if not head:
                head = ListNode(sum_digits[i - 1])
                tmp = head
            else:
                tmp.next = ListNode(sum_digits[i - 1])
                tmp = tmp.next

        return head


if __name__ == "__main__":
    l1 = to_node_list([7, 2, 4, 3])
    l2 = to_node_list([5, 6, 4])

    s = Solution()
    print(to_list(s.addTwoNumbers(l1, l2)))
    l1 = to_node_list([7, 3, 1])
    l2 = to_node_list([0])
    print(to_list(s.addTwoNumbers(l1, l2)))
