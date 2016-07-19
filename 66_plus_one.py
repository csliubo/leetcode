# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 反过来加
        if not digits:
            return [1]
        carry = False
        if digits[digits.__len__() - 1] + 1 >= 10:
            digits[digits.__len__() - 1] = 0
            carry = True
        else:
            digits[digits.__len__() - 1] = digits[digits.__len__() - 1] + 1
            return digits
        for i in range(digits.__len__() - 2, -1, -1):
            digit = digits[i]
            if carry:
                digit += 1
                if digit >= 10:
                    carry = True
                    digits[i] = 0
                else:
                    digits[i] = digit
                    carry = False
                    break
            else:
                break
        if carry:
            digits.insert(0, 1)
        return digits


s = Solution()
print s.plusOne([9])
print s.plusOne([])
print s.plusOne([0])
print s.plusOne([1])
print s.plusOne([1, 0])
print s.plusOne([1, 1])
print s.plusOne([9, 9, 9])
print s.plusOne([1, 0, 0, 0])
print s.plusOne([1, 0, 0, 1])
