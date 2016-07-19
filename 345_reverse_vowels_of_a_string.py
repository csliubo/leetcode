# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        if s.__len__() <= 1:
            return s
        head = 0
        tail = s.__len__() - 1
        head_chs = []
        tail_chs = []
        while head < tail:
            head_ch = s[head]
            tail_ch = s[tail]
            head_vowel = False
            tail_vowel = False
            if head_ch not in self.vowels:
                head += 1
                head_chs.append(head_ch)
            else:
                head_vowel = True
            if tail_ch not in self.vowels:
                tail_chs.append(tail_ch)
                tail -= 1
            else:
                tail_vowel = True
            if head_vowel and tail_vowel:
                head_chs.append(tail_ch)
                tail_chs.append(head_ch)
                head += 1
                tail -= 1
                head_vowel = False
                tail_vowel = False
            if head == tail:
                if head_vowel:
                    head_chs.append(head_ch)
                elif tail_vowel:
                    tail_chs.append(tail_ch)
                else:
                    head_chs.append(s[head])
        tail_chs = tail_chs[::-1]

        return "%s%s" % ("".join(head_chs), "".join(tail_chs))


s = Solution()
print s.reverseVowels("hell")
print s.reverseVowels(".a")
print s.reverseVowels("aeiouu")
print s.reverseVowels("leetcode")
print s.reverseVowels("a a")
