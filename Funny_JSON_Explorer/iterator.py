from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class NodeIterator(Iterator):

    _position: int = None

    _reverse: bool = False

    def __init__(self, collection: NodeCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class NodeCollection(Iterable):

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> NodeIterator:
        return NodeIterator(self)

    def get_reverse_iterator(self) -> NodeIterator:
        return NodeIterator(self, True)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)
