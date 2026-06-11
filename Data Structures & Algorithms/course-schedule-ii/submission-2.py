class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, preq in prerequisites:
            adj[course].append(preq)

        visit = set()
        res = []
        def dfs(course):
            nonlocal res
            if course in visit:
                res = []
                return False
            if course in res:
                return res

            visit.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    res = []
                    return False
            print("course: ", course)
            visit.remove(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res 