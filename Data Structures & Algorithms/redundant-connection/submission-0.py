class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        arr = [-1] * (len(edges) + 1)
        cycleSet = set()
        def find(node):
            if arr[node] < 0:
                return node

            arr[node] = find(arr[node])
            return arr[node]

        def union(a, b):
            rootA, rootB = find(a), find(b)
            if rootA == rootB:
                cycleSet.add((a, b))
                return
            if arr[rootA] <= arr[rootB]:
                arr[rootA] += arr[rootB]
                arr[rootB] = rootA
            else:
                arr[rootB] += arr[rootA]
                arr[rootA] = rootB
        
        for a, b in edges:
            union(a, b)

        for u, v in edges[::-1]:
            if (u, v) in cycleSet:
                return [u, v]

        return []
