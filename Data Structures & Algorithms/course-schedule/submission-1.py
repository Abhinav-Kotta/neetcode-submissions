class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            adj[course].append(preq)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if adj[course] == []:
                return True

            visit.add(course)
            for item in adj[course]:
                if not dfs(item):
                    return False

            visit.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True