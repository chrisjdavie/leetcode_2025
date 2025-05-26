class Trie:

    def __init__(self):
        self._prefix_trie: dict = [True, {}]

    def insert(self, word: str) -> None:
        curr: dict = self._prefix_trie
        for w in word:
            if w not in curr[1]:
                curr[1][w] = [False, {}]
            curr = curr[1][w]
        curr[0] = True

    def search(self, word: str) -> bool:
        curr: dict = self._prefix_trie
        for w in word:
            if w not in curr[1]:
                return False
            curr = curr[1][w]
        return curr[0]

    def startsWith(self, prefix: str) -> bool:
        curr: dict = self._prefix_trie
        for p in prefix:
            if p not in curr[1]:
                return False
            curr = curr[1][p]
        return True
