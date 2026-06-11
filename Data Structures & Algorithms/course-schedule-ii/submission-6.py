class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        visit = set()
        done = set()
        res = []

        for course, preq in prerequisites:
            preMap[course].append(preq)

        def dfs(course):
            nonlocal res
            if course in visit:
                return False

            if course in done:
                return True

            visit.add(course)
            for preq in preMap[course]:
                if not dfs(preq):
                    res = []
                    return False

            visit.remove(course)
            done.add(course)
            res.append(course)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []

        return res

        