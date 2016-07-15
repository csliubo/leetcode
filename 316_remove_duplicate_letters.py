# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # TODO 调整算法复杂度
        s_len = s.__len__()
        ret = ""

        # int_s = [ord(ch) for ch in s]

        for i in range(0, s_len):
            ch = s[i]
            if ch not in ret:
                # 未出现过的,直接加入
                ret += ch
            else:
                # 出现过的,判断在ret中已经存在的那位跟它后一位的关系
                index = ret.find(ch)
                if index == ret.__len__() - 1:
                    pass
                else:
                    k = i + 1
                    index_int = ord(ret[index])
                    if index_int - ord(ret[index + 1]) > 0:
                        ret = ret[:index] + ret[(index + 1):]
                        ret += ch
                    elif index < ret.__len__() - 2:
                        for j in range(index + 1, ret.__len__()):
                            if index_int - ord(ret[j]) > 0:
                                ret = ret[:index] + ret[(index + 1):]
                                ret += ch
                                break
                            else:
                                if s[k:].find(ret[j]) != -1:
                                    continue
                                else:
                                    break
        return ret



s = Solution()
# print s.removeDuplicateLetters("cbacdcbc")
# print s.removeDuplicateLetters("bcabc")
# print s.removeDuplicateLetters("mitnlruhznjfyzmtmfnstsxwktxlboxutbic")
# print s.removeDuplicateLetters("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws")
print s.removeDuplicateLetters("bxshkpdwcsjdbikywvioxrypfzfbppydfilfxxtouzzjxaymjpmdoevv")
# bfegkuyjrondiqszpcaw
# bfegkuyjorndiqszpcaw
print "bhcsdikworfltuzjxaympev"
