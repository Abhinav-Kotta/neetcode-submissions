class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}
        for course, preq in prerequisites:
            adjList[course].append(preq)

        visiting = set()
        done = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in done:
                return True

            visiting.add(crs)
            for preq in adjList[crs]:
                if not dfs(preq): return False
            
            visiting.remove(crs)
            done.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        