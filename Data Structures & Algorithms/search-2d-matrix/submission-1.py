class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows - 1

        upperBound = -1
        for row in range(rows):
            if matrix[row][cols - 1] > target:
                upperBound = row
                break
            elif matrix[row][cols - 1] >= target:
                return True
            else:
                continue

        if upperBound == -1:
            return False
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[upperBound][m] > target:
                r = m - 1
            elif matrix[upperBound][m] < target:
                l = m + 1
            else:
                return True
        return False