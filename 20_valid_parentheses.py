# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    m = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    left_part = {"(", "{", "["}
    right_part = {"}", "]", ")"}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        for part in s:
            if part in self.left_part:
                stack.append(part)
            elif part in self.right_part:
                if not stack:
                    return False
                top = stack[-1]
                if self.m.get(top) != part:
                    return False
                else:
                    stack.pop()

        if not stack:
            return True
        return False


s = Solution()

r = s.isValid("()[]{}")
print(r)
r = s.isValid("([]{}")
print(r)
r = s.isValid("([]{})")
print(r)
r = s.isValid("([)]")
print(r)
r = s.isValid("(]")
print(r)
