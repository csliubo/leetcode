# -*- coding:utf-8 -*-
import sys

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def getSum(self, a, b):
        """
        :type ret_xor: int
        :type ret_and: int
        :rtype: int
        """
        if a != b and abs(a) == abs(b):
            return 0
        ret_xor = a ^ b  # 筛选其中包含1的部分
        ret_and = a & b  # 筛选其中两个都为1的部分
        # print temp_xor, temp_and
        if ret_and != 0:
            ret_and <<= 1
            if ret_and:
                return self.getSum(ret_xor, ret_and)
        return ret_xor | ret_and

#用C/C++/Java可以用这种算法,Python会出问题

s = Solution()
print s.getSum(-14, 16)
