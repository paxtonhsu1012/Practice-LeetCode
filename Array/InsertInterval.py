### https://leetcode.com/problems/insert-interval/
### Medium

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, (start, end) in enumerate(intervals):
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > end:
                res.append([start, end])
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        res.append(newInterval)
        return res
