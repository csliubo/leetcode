from typing import List

from utils import ListNode, to_node_list

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if not head or not G:
            return 0
        nums = set([num for num in G])
        cur = head
        count = 0
        while cur:
            if cur.val in nums:
                count += 1
                while cur.next and cur.next.val in nums:
                    cur = cur.next
            cur = cur.next
        return count


if __name__ == "__main__":
    s = Solution()
    l1 = to_node_list([0, 1, 2, 3])
    g = [0, 1, 3]
    print(s.numComponents(l1, g))
    l1 = to_node_list([0, 1, 2, 3, 4])
    g = [0, 3, 1, 4]
    print(s.numComponents(l1, g))
