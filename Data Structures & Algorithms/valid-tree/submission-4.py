class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        arr = [-1] * n
        def find(node):
            if arr[node] < 0:
                return node
            
            arr[node] = find(arr[node])
            return arr[node]
            
        def union(a, b):
            rootA, rootB = find(a), find(b)
            print("pre union: ", a, b, rootA, rootB)
            if rootA == rootB:
                return False
            if arr[rootA] <= arr[rootB]:
                print("<= here values in root: ", arr[rootA], arr[rootB])
                arr[rootA] += arr[rootB]
                arr[rootB] = rootA
                print("after union in first condition: ", arr[rootA], arr[rootB])
            else:
                print("> here values in root: ", arr[rootA], arr[rootB])
                arr[rootB] += arr[rootA]
                arr[rootA] = rootB
                print("after union in second condition: ", arr[rootA], arr[rootB])

            return True


        for a, b in edges:
            if not union(a, b):
                return False
        return True