### https://leetcode.com/problems/k-closest-points-to-origin/
### Medium

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return None

        heap = [(points[i][0] ** 2 + points[i][1] ** 2, i) for i in range(len(points))]
        heapq.heapify(heap)

        ans = []
        while heap:
            tmp = heapq.heappop(heap)
            ans.append(points[tmp[1]])
            if len(ans) == k:
                break

        return ans
