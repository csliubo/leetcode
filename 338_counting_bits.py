# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        initial_counts = [0, 1, 1, 2]
        if num <= 3:
            return initial_counts[:num + 1]
        start = 3
        limit = pow(2, start) - 1
        current_counts = initial_counts
        while True:
            new_counts = [x + 1 for x in current_counts]
            if num > limit:
                current_counts.extend(new_counts)
            else:
                current_counts.extend(new_counts[:num - ((limit + 1) / 2) + 1])
                return current_counts
            start += 1
            limit = pow(2, start) - 1


s = Solution()
print s.countBits(3)
print s.countBits(5)
print s.countBits(7)
print s.countBits(11)
print s.countBits(15)
