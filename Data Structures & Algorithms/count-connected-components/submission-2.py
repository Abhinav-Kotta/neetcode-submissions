class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        arr = [-1] * n
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def find(node):
            if arr[node] < 0:
                return node
            arr[node] = find(arr[node])
            return arr[node]

        def union(a, b):
            rootA, rootB = find(a), find(b)
            if rootA == rootB:
                return
            if arr[rootA] <= arr[rootB]:
                arr[rootA] += arr[rootB]
                arr[rootB] = rootA
            else:
                arr[rootB] += arr[rootA]
                arr[rootA] = rootB

        for a, b in edges:
            union(a, b)

        res = 0
        for i in arr:
            if i < 0:
                res += 1

        return res