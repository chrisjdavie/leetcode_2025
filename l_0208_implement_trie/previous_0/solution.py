"""
I hadn't thought of using a sentinel in the dictionary to indicate EndOfWord.

As the reqs state inputs are "lowercase English letters" could use "*" as a
sentinel as well, but less general.

I was also messing about with recursive typing cos I don't know how to do that
"""
from typing import Optional

class EndOfWord:
    pass

Node = dict[str | EndOfWord, Optional['Node']]

class Trie:

    def __init__(self):
        self._prefix_trie: Node = {}

    def insert(self, word: str) -> None:
        curr: dict = self._prefix_trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr[EndOfWord] = None

    def _prefSearch(self, word: str) -> Node | bool:
        curr: dict = self._prefix_trie
        for w in word:
            if w not in curr:
                return False
            curr = curr[w]
        return curr

    def search(self, word: str) -> bool:
        if opp := self._prefSearch(word):
            return EndOfWord in opp
        return False

    def startsWith(self, prefix: str) -> bool:
        return bool(self._prefSearch(prefix))
