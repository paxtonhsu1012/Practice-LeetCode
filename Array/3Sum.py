### https://leetcode.com/problems/3sum/
### Medium

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []

        ans = []
        nums.sort()

        for i in range(len(nums)):
            target = -nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue

            m, n = i + 1, len(nums) - 1
            while m < n:
                if nums[i] + nums[m] + nums[n] == 0:
                    ans.append([nums[i], nums[m], nums[n]])
                    while m < n and nums[m+1] == nums[m]:
                        m += 1
                    while m < n and nums[n-1] == nums[n]:
                        n -= 1
                    m += 1
                    n -= 1
                elif nums[i] + nums[m] + nums[n] > 0:
                    n -= 1
                elif nums[i] + nums[m] + nums[n] < 0:
                    m += 1
        return ans
