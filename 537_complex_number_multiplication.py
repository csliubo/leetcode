# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Complex(object):
    def __init__(self, s):
        parts = s.split("+")
        self.real = int(parts[0])
        self.virtual = int(parts[1][:-1])

    def multiple(self, c):
        real = self.real * c.real - (self.virtual * c.virtual)
        virtual = self.real * c.virtual + self.virtual * c.real
        return "%s+%si" % (real, virtual)

    def __repr__(self):
        return "%s+%si" % (self.real, self.virtual)


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        complex_a = Complex(a)
        return complex_a.multiple(Complex(b))


s = Solution()
a, b = "1+1i", "1+1i"
a, b = "1+-1i", "1+-1i"
print s.complexNumberMultiply(a, b)
