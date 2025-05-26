class Trie:

    def __init__(self):
        self._words: set[str] = set()

    def insert(self, word: str) -> None:
        self._words.add(word)

    def search(self, word: str) -> bool:
        return word in self._words

    def startsWith(self, prefix: str) -> bool:
        for word in self._words:
            if word.startswith(prefix):
                return True
        return False
