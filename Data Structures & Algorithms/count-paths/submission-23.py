from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def f(r,c):
            if r >= m or c >= n: return 0
            if r == m - 1 and c == n - 1: return 1
            return f(r+1,c)+f(r,c+1)
        return f(0,0)