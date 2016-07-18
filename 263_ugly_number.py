# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num <= 3:
            return True

        while num > 1:
            need_continue = False
            for factor in [2, 3, 5]:
                if num % factor == 0:
                    num /= factor
                    need_continue = True
                    break
            if need_continue:
                continue
            return False
        return True


s = Solution()
print s.isUgly(2)
print s.isUgly(6)
print s.isUgly(10)
print s.isUgly(14)
print s.isUgly(8)
