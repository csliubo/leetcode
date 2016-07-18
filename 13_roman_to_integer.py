# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]
'''
罗马数字共有七个，即I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)。按照下面的规则可以表示任意正整数。
重复数次：一个罗马数字重复几次，就表示这个数的几倍。
右加左减：在一个较大的罗马数字的右边记上一个较小的罗马数字，表示大数字加小数字。在一个较大的数字的左边记上一个较小的罗马数字，表示大数字减小数字。但是，左减不能跨越一个位数。比如，99不可以用IC表示，而是用XCIX表示。此外，左减数字不能超过一位，比如8写成VIII，而非IIX。同理，右加数字不能超过三位，比如十四写成XIV，而非XIIII。
单位限制：同样单位只能出现3次，如40不能表示为XXXX，而要表示为XL。
'''


class Solution(object):
    _roman_int_ = {
        'I': 1,
        'II': 2,
        'III': 3,
        'IV': 4,
        'V': 5,
        'VI': 6,
        'VII': 7,
        'VIII': 8,
        'IX': 9,
        'X': 10,
        'XX': 20,
        'XXX': 30,
        'XL': 40,
        'L': 50,
        'LX': 60,
        'LXX': 70,
        'LXXX': 80,
        'XC': 90,
        'C': 100,
        'CC': 200,
        'CCC': 300,
        'CD': 400,
        'D': 500,
        'DC': 600,
        'DCC': 700,
        'DCCC': 800,
        'CM': 900,
        'M': 1000,
        'MM': 2000,
        'MMM': 3000
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s_len = s.__len__()
        ret = 0
        i = 0
        while i < s_len:
            if s_len - i > 4:
                offset_max = 4
            else:
                offset_max = s_len - i
            for offset in xrange(offset_max, 0, -1):
                ch = s[i:i + offset]
                if ch in self._roman_int_:
                    current_val = self._roman_int_.get(ch)
                    ret += current_val
                    i += offset

                    break
        return ret


s = Solution()
# print s.romanToInt('I')
# print s.romanToInt('II')
# print s.romanToInt('III')
# print s.romanToInt('IV')
# print s.romanToInt('V')
# print s.romanToInt('VI')
# print s.romanToInt('VII')
# print s.romanToInt('VIII')
# print s.romanToInt('IX')
# print s.romanToInt('X')
# print s.romanToInt('XI')
# print s.romanToInt('XII')
# print s.romanToInt('XIII')
# print s.romanToInt('XIV')
# print s.romanToInt('XV')
# print s.romanToInt('XVI')
# print s.romanToInt('XVII')
# print s.romanToInt('XVIII')
# print s.romanToInt('XIX')
# print s.romanToInt('XX')
# print s.romanToInt('XXI')
# print s.romanToInt('XXII')
# print s.romanToInt('XXVIII')
# print s.romanToInt('XXIX')
# print s.romanToInt('XXX')
# print s.romanToInt('XL')
# print s.romanToInt('L')
# print s.romanToInt('LX')
# print s.romanToInt('LXX')
# print s.romanToInt('LXXX')
# print s.romanToInt('XC')
# print s.romanToInt('XCIX')
# print s.romanToInt('C')
# print s.romanToInt('CI')
# print s.romanToInt('CXCIX')
# print s.romanToInt('CC')
# print s.romanToInt('CCC')
# print s.romanToInt('CD')
# print s.romanToInt('D')
print s.romanToInt('DCLXVI')
# print s.romanToInt('M')
print s.romanToInt('MCMXCIX')
# print s.romanToInt('MM')
# print s.romanToInt('MMM')
print s.romanToInt('MMMCMXCIX')