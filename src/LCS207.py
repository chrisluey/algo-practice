from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = [[] for i in range(numCourses)]
        num_prereqs = [0 for i in range(numCourses)]
        visited = []
        no_edges = deque()
        for a, b in prerequisites:
            num_prereqs[a] += 1
            prereqs[b].append(a)
        for i in range(len(num_prereqs)):
            if num_prereqs[i] == 0:
                no_edges.append(i)
        while len(no_edges) > 0:
            curr = no_edges.popleft()
            visited.append(curr)
            for j in prereqs[curr]:
                num_prereqs[j] -= 1
                if num_prereqs[j] == 0:
                    no_edges.append(j)
        return len(visited) == numCourses