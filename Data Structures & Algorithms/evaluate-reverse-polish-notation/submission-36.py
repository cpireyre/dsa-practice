class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        xs = []
        for t in tokens:
            if t == "+":
                a,b = xs.pop(), xs.pop()
                xs.append(a+b)
            elif t == "*":
                a,b = xs.pop(), xs.pop()
                xs.append(a*b)
            elif t == "-":
                a,b = xs.pop(), xs.pop()
                xs.append(b-a)
            elif t == "/":
                a,b = xs.pop(), xs.pop()
                xs.append(int(b/a))
            else: xs.append(int(t))
        return xs[0]