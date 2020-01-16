# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret = x ^ y
        count = 0
        for ch in bin(ret)[2:]:
            if ch == "1":
                count += 1
        return count


s = Solution()
print s.hammingDistance(1, 4)
