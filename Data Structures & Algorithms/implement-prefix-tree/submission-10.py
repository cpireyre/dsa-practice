class PrefixTree:
    def __init__(self):
        self.children = defaultdict(PrefixTree)
        self.word = False

    def insert(self, word: str) -> None:
        root = self
        for c in word: root = root.children[c]
        root.word = True

    def search(self, word: str) -> bool:
        root = self
        for c in word:
            if c not in root.children: return False
            root = root.children[c]
        return root.word

    def startsWith(self, prefix: str) -> bool:
        root = self
        for c in prefix:
            if c not in root.children: return False
            root = root.children[c]
        return True