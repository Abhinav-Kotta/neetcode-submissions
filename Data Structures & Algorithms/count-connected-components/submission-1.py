class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        arr = [-1] * n
        def find(node):
            if arr[node] < 0:
                return node
            arr[node] = find(arr[node])
            return arr[node]

        def union(a, b):
            print(a, b)
            rootA, rootB = find(a), find(b)
            if rootA == rootB:
                return
            if arr[rootA] <= arr[rootB]:
                arr[rootA] += arr[rootB]
                arr[rootB] = rootA
            else:
                arr[rootB] += arr[rootA]
                arr[rootA] = rootB

        res = 0
        for a, b in edges:
            union(a, b)

        for ele in arr:
            if ele < 0:
                res += 1

        return res

            