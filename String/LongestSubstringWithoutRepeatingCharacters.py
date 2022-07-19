###
### Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        dic = {}
        head = tail = 0
        maxlen = float(-inf)

        for c in s:
            if c in dic:
                if dic[c] >= head:
                    maxlen = max(maxlen, tail - head)
                    head = dic[c] + 1
            dic[c] = tail
            tail += 1
        maxlen = max(maxlen, tail - head)
        return maxlen
