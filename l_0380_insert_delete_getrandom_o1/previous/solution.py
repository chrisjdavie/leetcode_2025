import random

class RandomizedSet:

    def __init__(self):
        self._item_to_pos: dict[int, int] = {}
        self._items: list[int] = []

    def insert(self, val: int) -> bool:
        if val in self._item_to_pos:
            return False
        self._item_to_pos[val] = len(self._items)
        self._items.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._item_to_pos:
            return False
        pos: int = self._item_to_pos.pop(val)
        val_last: int = self._items.pop()
        if val_last != val:
            self._items[pos] = val_last
            self._item_to_pos[val_last] = pos
        return True

    def getRandom(self) -> int:
        return random.choice(self._items)
