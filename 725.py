from typing import List

from utils import ListNode, to_node_list, to_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not root:
            return None
        if k == 1:
            return [root]
        cur = root
        node_count = 0
        while cur:
            cur, node_count = cur.next, node_count + 1

        ret = [[]] * k
        avg_len = int(node_count / k)
        plus_one_position = node_count % k
        prev, cur = None, root
        for i in range(0, k):
            current_len = avg_len
            if i < plus_one_position:
                current_len += 1
            ret[i] = cur
            j = 0
            while j < current_len:
                prev, cur, j = cur, cur.next, j + 1
            prev.next = None

        return ret


if __name__ == "__main__":


    s = Solution()
    l1 = to_node_list([8, 4, 3, 2, 5, 2, 7])
    print([to_list(i) for i in s.splitListToParts(l1, 3)])
    l1 = to_node_list([8, 4, 3, 2, 5, 2, 7])
    print([to_list(i) for i in s.splitListToParts(l1, 1)])
    l1 = to_node_list([8, 4, 3, 2, 5, 2, 7])
    print([to_list(i) for i in s.splitListToParts(l1, 7)])
    l1 = to_node_list([])
    # print([to_list(i) for i in s.splitListToParts(l1, 7)])
    l1 = to_node_list([1])
    print([to_list(i) for i in s.splitListToParts(l1, 7)])
    # l1 = to_node_list([])
    # print(to_list(s.splitListToParts(l1, 3)))
