from __future__ import annotations
from abc import ABC, abstractmethod
import style


class Context:

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def operation(self, factory, node):
        self._strategy.do_algorithm(factory, node)


class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, node):
        pass


class ContainerStrategy(Strategy):
    def do_algorithm(self, factory, node):
        factory.render_container_node(factory, node)


class LeafStrategy(Strategy):
    def do_algorithm(self, factory, node):
        factory.render_leaf_node(factory, node)
