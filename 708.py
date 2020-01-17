from utils import to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        if not head.next:
            head.next = Node(insertVal, next=head)
            return head
        prev, cur = head, head.next
        while cur:
            if (prev.val <= insertVal <= cur.val) or (insertVal >= prev.val >= cur.val):
                prev.next = Node(insertVal, next=cur)
                return head
            prev, cur = cur, cur.next
        return head


if __name__ == "__main__":
    s = Solution()
    l1 = to_node_list([])
    print(to_list(s.insert(l1, 2)))

    l1 = to_node_list([1, 2, 3])
    print(to_list(s.insert(l1, 2)))
