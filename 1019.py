from typing import List

from utils import to_node_list, ListNode, compare_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return None
        index_map = {}
        node_stack = []
        ret = []
        cur = head
        index = 0
        while cur:
            # push into stack
            index_map[cur] = index
            ret.append(0)
            while node_stack and node_stack[-1].val < cur.val:
                node = node_stack.pop()
                ret[index_map[node]] = cur.val
            node_stack.append(cur)
            cur, index = cur.next, index + 1
        return ret

    def reverse(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            prev, cur.next, cur = cur, prev, cur.next

        return prev


if __name__ == "__main__":
    s = Solution()
    s = Solution()
    l1 = to_node_list([1, 7, 5, 1, 9, 2, 5, 1])
    print(s.nextLargerNodes(l1))
    # assert (s.nextLargerNodes(l1) == [7, 9, 9, 9, 0, 5, 0, 0])
    # l1 = to_node_list([2, 1, 5])
    # assert (s.nextLargerNodes(l1) == [5, 5, 0])
