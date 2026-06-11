class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        target_row, target_col = -1, 0
        for r in range(rows):
            print(matrix[r][0])
            if target < matrix[r][0]:
                target_row = r - 1
                break
            elif target == matrix[r][0]:
                return True

        if target_row == -1:
            target_row = rows - 1

        l, r = 0, cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target > matrix[target_row][mid]:
                l = mid + 1
            elif target < matrix[target_row][mid]:
                r = mid - 1
            else:
                return True

        return False
