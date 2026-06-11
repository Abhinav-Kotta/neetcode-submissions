class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        visit = set()

        for node, edge in edges:
            adjList[node].append(edge)
            adjList[edge].append(node)

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for nei in adjList[node]:
                dfs(nei)

        components = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                components += 1

        return components

                

