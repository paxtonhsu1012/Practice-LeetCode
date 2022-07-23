### https://leetcode.com/problems/course-schedule/
### Medium

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for i in range(numCourses)]
        degree = [0] * numCourses

        for nxt, pre in prerequisites:
            graph[pre].append(nxt)
            degree[nxt] += 1

        s = []
        for i in range(numCourses):
            if degree[i] == 0:
                s.append(i)

        for pre in s:
            for nxt in graph[pre]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    s.append(nxt)

        return len(s) == numCourses
