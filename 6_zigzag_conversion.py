# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        len = s.__len__()
        ret = []
        for i in range(0, numRows):
            ret.append("")
        for i in range(0, len):
            if i / (numRows - 1) % 2 == 0:
                row = i % (numRows - 1)
            else:
                row = (numRows - 1) - i % (numRows - 1)
            ret[row] += s[i]
        ret_str = "".join(ret[i] for i in range(0, ret.__len__()))

        return ret_str


s = Solution()
print s.convert("PAYPALISHIRING", 3)
print s.convert("PAYPALISHIRING", 1)
print s.convert("PAYPALISHIRING", 2)
