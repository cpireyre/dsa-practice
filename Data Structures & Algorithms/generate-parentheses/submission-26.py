class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def f(acc,o,c):
            if o == c == n:
                res.append(acc)
                return
            if o < n: f(acc + "(", o+1, c)
            if c < o: f(acc + ")", o, c+1)
        f("",0,0)
        return res