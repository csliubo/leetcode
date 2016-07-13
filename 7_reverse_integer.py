# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -9 <= x <= 9:
            return x
        is_negative = False
        if x < 0:
            is_negative = True
        min_int = - 2147483648
        max_int = 2147483647
        if x <= min_int:
            return 0
        ret = 0
        x = abs(x)
        while (x >= 1):
            digit = x % 10
            if ret:
                ret = ret * 10 + digit
            else:
                if digit:
                    ret = digit
            x = x / 10
        if ret > max_int or ret < min_int:
            return 0
        if is_negative:
            return -ret
        return ret


s = Solution()
print s.reverse(0)
print s.reverse(10)
print s.reverse(-10)
print s.reverse(-11)
print s.reverse(9223372036854775899)
