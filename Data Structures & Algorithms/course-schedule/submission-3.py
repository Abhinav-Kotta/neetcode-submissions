class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        visit = set()
        for course, pre in prerequisites:
            adj[course].append(pre)

        def dfs(course):
            if adj[course] == []:
                return True
            if course in visit:
                return False

            visit.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            visit.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True