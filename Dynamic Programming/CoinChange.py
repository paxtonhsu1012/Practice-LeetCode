### https://leetcode.com/problems/coin-change/
### Medium

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dp(num):

            if num == 0:
                return 0
            if num < 0:
                return -1

            res = float(inf)
            for c in coins:
                tmp = dp(num - c)
                if tmp != -1:
                    res = min(res, tmp + 1)

            return res if res != float(inf) else -1

        return dp(amount)
