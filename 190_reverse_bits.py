# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def reverseBits(self, n: int) -> int:
        i, ret = 32, 0
        while i:
            ret = ret | (n & 1)
            n >>= 1
            ret <<= 1
            i -= 1
        return ret


s = Solution()
print(s.reverseBits(1))
print(s.reverseBits(43261596))
