# -*- coding:utf-8 -*-

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len = s.__len__()
        if len <= 1:
            return s

        result = None
        for n in self.re_index(len):
            # 第一种情况，以n为中心，判断n+1,n-1是否相等
            limit = min(len - n - 1, n)
            result_one = s[n]
            for i in range(1, limit + 1):
                if (s[n - i] == s[n + i]):
                    result_one = s[n - i:n + i + 1]
                else:
                    break

            # 第二种情况，从n开始，判断n,n+1是否相等

            limit = min(len - n - 2, n)

            result_two = s[n]

            for i in range(0, limit + 1):
                if (s[n - i] == s[n + i + 1]):
                    result_two = s[n - i:n + i + 2]
                else:
                    break
            if not result_two:
                result_two = s[n]
            max_result = result_one if result_one.__len__() >= result_two.__len__() else result_two

            if not result:
                result = max_result
            elif max_result.__len__() >= result.__len__():
                result = max_result

            if result.__len__() > 1 and result.__len__() >= 2 * min(len - n - 1, n) + 1:
                return result
        return result

    def re_index(self, len):
        ret = []
        middle = (len - 1) / 2
        ret.append(middle)
        if len % 2 == 0:
            for i in range(1, middle + 1):
                ret.append(middle + i)
                ret.append(middle - i)
            ret.append(len - 1)
        else:
            for i in range(1, middle + 1):
                ret.append(middle - i)
                ret.append(middle + i)

        return ret


val = '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

s = Solution()
print val.__len__()
print s.longestPalindrome(val)
print s.longestPalindrome("bb")
print s.longestPalindrome("ccd")
print s.longestPalindrome("abb")
val = "jrjnbctoqgzimtoklkxcknwmhiztomaofwwzjnhrijwkgmwwuazcowskjhitejnvtblqyepxispasrgvgzqlvrmvhxusiqqzzibcyhpnruhrgbzsmlsuacwptmzxuewnjzmwxbdzqyvsjzxiecsnkdibudtvthzlizralpaowsbakzconeuwwpsqynaxqmgngzpovauxsqgypinywwtmekzhhlzaeatbzryreuttgwfqmmpeywtvpssznkwhzuqewuqtfuflttjcxrhwexvtxjihunpywerkktbvlsyomkxuwrqqmbmzjbfytdddnkasmdyukawrzrnhdmaefzltddipcrhuchvdcoegamlfifzistnplqabtazunlelslicrkuuhosoyduhootlwsbtxautewkvnvlbtixkmxhngidxecehslqjpcdrtlqswmyghmwlttjecvbueswsixoxmymcepbmuwtzanmvujmalyghzkvtoxynyusbpzpolaplsgrunpfgdbbtvtkahqmmlbxzcfznvhxsiytlsxmmtqiudyjlnbkzvtbqdsknsrknsykqzucevgmmcoanilsyyklpbxqosoquolvytefhvozwtwcrmbnyijbammlzrgalrymyfpysbqpjwzirsfknnyseiujadovngogvptphuyzkrwgjqwdhtvgxnmxuheofplizpxijfytfabx"
print s.longestPalindrome(val)
