import glob
from os.path import dirname, basename
from importlib import import_module

from typing import Dict, Iterator, Tuple, Callable


class _storage():

    def __init__(self):
        self._dict: Dict[str, Callable] = {}

    def items(self) -> Iterator[Tuple[str, Callable]]:
        for k, v in self._dict.items():
            yield (k, v)

    def keys(self) -> Iterator[str]:
        for k in self._dict.keys():
            yield k

    def values(self) -> Iterator[Callable]:
        for v in self._dict.values():
            yield v

    def __setitem__(self, key: str, value: Callable) -> None:
        if key.upper() in self._dict:
            raise ValueError("Stored Cards are readonly")
        self._dict[key.upper()] = value

    def __getattr__(self, key) -> Callable:
        if key.upper() in self._dict:
            return self._dict[key.upper()]

        raise LookupError("%s not found", key)

    def __getitem__(self, key) -> Callable:
        return self.__getattr__(key)


Cards = _storage()
for card in glob.glob(dirname(__file__) + "/*"):
    if ".py" in basename(card):
        continue
    Cards[basename(card)] = import_module("easydecks.cards.%s" % basename(card))
