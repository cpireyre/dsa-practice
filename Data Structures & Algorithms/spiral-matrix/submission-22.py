class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R,C = len(matrix),len(matrix[0])
        steps = [C,R-1]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        r,c,d = 0,-1,0
        res = []
        while steps[d&1]:
            dr,dc = dirs[d]
            for _ in range(steps[d&1]):
                r += dr; c += dc
                res.append(matrix[r][c])
            steps[d&1] -= 1
            d = (d+1)%4
        return res