class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for dst, src in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        queue = collections.deque()
        for course_id, indeg in enumerate(indegree):
            if indeg == 0:
                queue.append(course_id)
        
        num_visited = 0
        while queue:
            course_id = queue.popleft()
            num_visited += 1

            # visit the neighbour and decrease their indegree
            for nei in adj[course_id]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return num_visited == numCourses

