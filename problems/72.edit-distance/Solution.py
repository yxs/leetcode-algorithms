class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        if n * m == 0:
            return n + m

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # dp[i][j] 表示 word1 的前 i 个字母和 word2 的前 j 个字母之间的编辑距离
        # init
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        # 对 word1 进行操作，得到 word2
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 跳过
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 删除 word1[i]，因此前移，i - 1｜插入｜替换
                    dp[i][j] = min(
                        dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1
                    )

        return dp[n][m]
