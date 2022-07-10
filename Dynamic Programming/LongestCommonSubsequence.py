### https://leetcode.com/problems/longest-common-subsequence/
### Medium

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m1 = len(text1)
        m2 = len(text2)

        rec = [[ 0 for _ in range(m2+1) ] for _ in range(m1+1)]

        for i in range(1, m1+1):
            for j in range(1, m2+1):
                if text1[i-1] == text2[j-1]:
                    rec[i][j] = rec[i-1][j-1] + 1
                else:
                    rec[i][j] = max(rec[i-1][j], rec[i][j-1])

        return rec[m1][m2]
