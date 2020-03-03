__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def numPermsDISequence(self, S: str) -> int:
        MOD = 10 ** 9 + 7

        def cal(i, j):
            if not (0 <= j <= i):
                return 0
            if i == 0:
                return 1
            elif S[i - 1] == "D":
                return (cal(i, j + 1) + cal(i - 1, j )) % MOD
            else:
                return (cal(i - 1, j - 1) + cal(i, j - 1)) % MOD

        return sum(cal(len(S), i) for i in range(0, len(S) + 1)) % MOD


if __name__ == "__main__":
    s = Solution()
    ret = s.numPermsDISequence("DID")
    print(ret)
