class Trie:

    def __init__(self):
        self._prefix_trie: dict = {}
        self._words: set = set()

    def insert(self, word: str) -> None:
        self._words.add(word)
        curr: dict = self._prefix_trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]

    def search(self, word: str) -> bool:
        return word in self._words

    def startsWith(self, prefix: str) -> bool:
        curr: dict = self._prefix_trie
        for p in prefix:
            if p not in curr:
                return False
            curr = curr[p]
        return True
