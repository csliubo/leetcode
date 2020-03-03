__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def count_one(self, num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    def countPrimeSetBits(self, L: int, R: int) -> int:
        ret = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        for i in range(L, R + 1):
            num = i
            count = 0
            while num:
                count += num & 1
                num >>= 1

            if count in primes:
                ret += 1
        return ret
