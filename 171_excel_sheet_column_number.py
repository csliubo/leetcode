# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for ch in s:
            int_val = ord(ch) - ord('A') + 1
            if ret:
                ret = ret * 26 + int_val
            else:
                ret = int_val
        return ret


s = Solution()
print s.titleToNumber('A')
print s.titleToNumber('B')
print s.titleToNumber('Y')
print s.titleToNumber('Z')
print s.titleToNumber('AA')
print s.titleToNumber('AB')
