class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def f(xs,O,C):
            if O == C == n:
                res.append("".join(xs[:]))
                return
            if O < n:
                xs.append("(")
                f(xs,O+1,C)
                xs.pop()
            if C < O:
                xs.append(")")
                f(xs,O,C+1)
                xs.pop()
        f([],0,0)
        return res