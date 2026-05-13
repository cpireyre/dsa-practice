class WordDictionary:
    def __init__(self):
        self.children = defaultdict(WordDictionary)
        self.word = False

    def addWord(self, word: str) -> None:
        root = self
        for c in word: root = root.children[c]
        root.word = True

    def search(self, word: str) -> bool:
        def f(node,l):
            if l == len(word): return node.word
            for r,c in enumerate(word[l:]):
                if c == '.':
                    return any(f(C,l+r+1) for C in node.children.values())
                elif c not in node.children: return False
                node = node.children[c]
            return node.word
        return f(self,0)