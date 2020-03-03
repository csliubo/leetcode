# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def countDigitOne(self, n: int) -> int:
        reversed_nums = reversed(str(n))
        count = 0
        passed_num = 0
        for i, num in enumerate(reversed_nums):
            num = int(num)
            if num == 1:
                if i > 0:
                    base = i * (10 ** (i - 1))
                    count += passed_num + 1 + base
                else:
                    count += passed_num + 1 + base
            elif num > 1:
                if i > 0:
                    base = i * (10 ** (i - 1))
                    count += num * base + (10 ** i)
                else:
                    count = 1
            passed_num += int(num) * (10 ** i)
            # print(count, passed_num, i)
        return count


s = Solution()
# print(s.countDigitOne(5))
# print(s.countDigitOne(1808548329))
print(s.countDigitOne(1876))
print(s.countDigitOne(876))
print(s.countDigitOne(76))
print(s.countDigitOne(6))
print(s.countDigitOne(0))
print(s.countDigitOne(9))
print(s.countDigitOne(99))
print(s.countDigitOne(999))
print(s.countDigitOne(9999))
