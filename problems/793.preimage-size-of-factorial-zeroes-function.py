class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        # zeta(x) 为 x! 末尾零的个数
        def zeta(x):
            return x // 5 + zeta(x // 5) if x > 0 else 0

        lo, hi = K, 10 * K + 1
        while lo < hi:
            mi = (lo + hi) // 2
            zmi = zeta(mi)
            if zmi == K:
                return 5
            elif zmi < K:
                lo = mi + 1
            else:
                hi = mi

        return 0
