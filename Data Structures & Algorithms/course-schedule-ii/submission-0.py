class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        visit, res = set(), []
        for course, preq in prerequisites:
            adj[course].append(preq)

        def dfs(course):
            nonlocal res
            if course in visit:
                print("in visit")
                res = []
                return False
            if course in res:
                return res

            visit.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    res = []
                    return False
            visit.remove(course)
            res.append(course)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res