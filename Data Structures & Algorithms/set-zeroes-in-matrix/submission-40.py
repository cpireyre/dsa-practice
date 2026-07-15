class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R,C = len(matrix),len(matrix[0])
        shouldClearTop = False
        for r,c in product(range(R),range(C)):
            if matrix[r][c] == 0:
                if r == 0: shouldClearTop = True
                else: matrix[r][0] = 0
                matrix[0][c] = 0
        for r,c in product(range(1,R),range(1,C)):
            if matrix[0][c]*matrix[r][0] == 0: matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(R): matrix[r][0] = 0
        if shouldClearTop:
            for c in range(C): matrix[0][c] = 0