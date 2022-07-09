### https://leetcode.com/problems/climbing-stairs/
### Easy

class Solution:
    def climbStairs(self, n: int) -> int:
        rec = [1, 1]

        for i in range(2, n+1):
            rec.append(rec[i-1] + rec[i-2])

        return rec[n]
