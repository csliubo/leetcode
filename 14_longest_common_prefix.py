# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        ch_index = 0
        ret = ""
        str_count = strs.__len__()
        while True:
            if ch_index >= strs[0].__len__():
                return ret
            ch = strs[0][ch_index]
            for i in range(1, str_count):
                if ch_index >= strs[i].__len__():
                    return ret

                if ch != strs[i][ch_index]:
                    return ret
            ret += ch
            ch_index += 1


s = Solution()

print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["car", "ar", "are"]))
print(s.longestCommonPrefix(["", "ar", "are"]))
print(s.longestCommonPrefix(["a", "ar", "are"]))
