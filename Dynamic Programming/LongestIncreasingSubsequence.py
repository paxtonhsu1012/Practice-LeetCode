### https://leetcode.com/problems/longest-increasing-subsequence/
### Medium

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [1] * len(nums)
        for k in range(1, len(nums)):
            for idx in range(k):
                if nums[k] > nums[idx]:
                    result[k] = max(result[idx] + 1, result[k])

        return max(result)
