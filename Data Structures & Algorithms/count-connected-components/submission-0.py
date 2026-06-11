class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        count = 0
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        def dfs(node):
            if node in visit:
                return

            visit.add(node)
            for nei in adj[node]:
                dfs(nei)


        for a in adj:
            if a in visit:
                continue
            else:
                dfs(a)
                count += 1

        return count + (n - len(visit))