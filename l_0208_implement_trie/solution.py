"""
I hadn't thought of using a sentinel in the dictionary to indicate EndOfWord.

As the reqs state inputs are "lowercase English letters" could use "*" as a
sentinel as well, but less general.

I was also messing about with recursive typing cos I don't know how to do that
"""
END_OF_WORD: str = "end_of_word"

class Trie:

    def __init__(self):
        self._prefix_trie: dict[str, dict | None] = {}

    def insert(self, word: str) -> None:
        curr: dict[str, dict | None] = self._prefix_trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr[END_OF_WORD] = None

    def search(self, word: str) -> bool:
        curr: dict[str, dict | None] = self._prefix_trie
        for w in word:
            if w not in curr:
                return False
            curr = curr[w]
        return END_OF_WORD in curr

    def startsWith(self, prefix: str) -> bool:
        curr: dict[str, dict | None] = self._prefix_trie
        for w in prefix:
            if w not in curr:
                return False
            curr = curr[w]
        return True
