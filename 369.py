from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if head.val == 0:
            head.val = 1
            return head
        tail = self.reverse(head)
        cur = tail
        carry_digit = False
        cur.val += 1
        if cur.val >= 10:
            cur.val -= 10
            carry_digit = True
        prev, cur = cur, cur.next
        while cur:
            if carry_digit:
                carry_digit = False
                cur.val = cur.val + 1
            if cur.val >= 10:
                cur.val -= 10
                carry_digit = True
            prev, cur = cur, cur.next
        if carry_digit:
            prev.next = ListNode(1)
        return self.reverse(tail)

    def reverse(self, head):
        prev, cur = None, head
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        return prev


if __name__ == "__main__":
    s = Solution()
    l1 = to_node_list([1, 2, 3, 3, 4])
    print(to_list(s.plusOne(l1)))
    l1 = to_node_list([1, 2, 3, 3, 9])
    print(to_list(s.plusOne(l1)))
    l1 = to_node_list([9])
    print(to_list(s.plusOne(l1)))
    l1 = to_node_list([9, 9])
    print(to_list(s.plusOne(l1)))
    l1 = to_node_list([0])
    print(to_list(s.plusOne(l1)))