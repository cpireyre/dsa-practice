class WordDictionary:
    def __init__(self):
        self.children = defaultdict(WordDictionary)
        self.word = False

    def addWord(self, word: str) -> None:
        root = self
        for c in word: root = root.children[c]
        root.word = True

    def search(self, word: str) -> bool:
        def f(root,l):
            if l == len(word): return root.word
            for r,c in enumerate(word[l:]):
                if c == '.':
                    return any(f(n,l+r+1) for n in root.children.values())
                elif c not in root.children: return False
                root = root.children[c]
            return root.word
        return f(self,0)