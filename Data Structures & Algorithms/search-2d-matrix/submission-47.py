class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R,C = len(matrix),len(matrix[0])
        l,r = 0,R*C-1
        while l <= r:
            m = l + (r-l)//2
            v = matrix[m//C][m%C]
            if   v > target: r = m - 1
            elif v < target: l = m + 1
            else:            return True
        return False