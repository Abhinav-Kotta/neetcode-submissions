class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        array = [-1] * (len(edges) + 1)
        cycleSet = set()
        
        def find(node):
            if array[node] < 0:
                return node

            array[node] = find(array[node])
            return array[node]


        def union(a, b):
            rootA, rootB = find(a), find(b)
            if rootA == rootB:
                cycleSet.add((a, b))
                return

            if array[rootA] <= array[rootB]:
                array[rootA] += array[rootB]
                array[rootB] = rootA
            else:
                array[rootB] += array[rootA]
                array[rootA] = rootB

            

        for a, b in edges:
            union(a, b)

        for u, v in edges[::-1]:
            if (u, v) in cycleSet:
                return [u, v]

        return []
