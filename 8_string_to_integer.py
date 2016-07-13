# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        is_negative = False
        result = 0
        str = str.strip()  # 去除前置空白字符
        if str[0] in ['+', '-']:
            if str[0] == '-':
                is_negative = True
            str = str[1:]
        if not str:
            return 0
        if str[0] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return 0
        for ch in str:
            if ch in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if result:
                    result = result * 10 + int(ch)
                else:
                    ch != '0'
                    result = int(ch)
            else:
                break
        if is_negative:
            result = -result
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        return result
