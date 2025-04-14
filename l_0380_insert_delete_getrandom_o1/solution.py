from random import choice


class RandomizedSet:

    def __init__(self):
        self._vals: list[int] = []
        self._vals_index: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self._vals_index:
            return False
        self._vals_index[val] = len(self._vals)
        self._vals.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self._vals_index:
            return False
        last_val: int = self._vals.pop()
        val_ind: int = self._vals_index.pop(val)
        if val != last_val:
            self._vals_index[last_val] = val_ind
            self._vals[val_ind] = last_val
        return True

    def getRandom(self) -> int:
        return choice(self._vals)
