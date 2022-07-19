### https://leetcode.com/problems/01-matrix/
### Medium

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                    continue
                mat[i][j] = float(inf)

        directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        while q:
            tmp = q.popleft()
            dist = mat[tmp[0]][tmp[1]]
            for d in directions:
                r, c = tmp[0] + d[0], tmp[1] + d[1]

                if r in range(m) and c in range(n) and mat[r][c] != 0:
                    if dist + 1 < mat[r][c]:
                        mat[r][c] = dist + 1
                        q.append((r, c))
        return mat
