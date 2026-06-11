class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        lCol, rCol = 0, len(matrix) - 1
        # number of rotations is n - 1
        # do rotations from outwards in
        # do rotations in reverse to not make as many temoprary pointers

        while lCol < rCol:
            for i in range(rCol - lCol):
                topRow, bottomRow = lCol, rCol

                # top left
                topLeft = matrix[topRow][lCol + i]
                matrix[topRow][lCol + i] = matrix[bottomRow - i][lCol]

                # bottom left
                matrix[bottomRow - i][lCol] = matrix[bottomRow][rCol - i]

                # bottom right
                matrix[bottomRow][rCol - i] = matrix[topRow + i][rCol]

                # top right
                matrix[topRow + i][rCol] = topLeft

            rCol -= 1
            lCol += 1
