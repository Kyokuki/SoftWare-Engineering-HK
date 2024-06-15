from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import strategy


class Node(ABC):

    def __init__(self):
        self.key = None
        self.value = None
        self.depth = 0
        self.is_first = False
        self.is_last = False
        self.icon = None
        self.node_parent = None

    @property
    def parent(self) -> Node:
        return self.node_parent

    @parent.setter
    def parent(self, parent: Node):
        self.node_parent = parent

    def add(self, component: Node) -> None:
        pass

    def remove(self, component: Node) -> None:
        pass

    def is_container(self) -> bool:
        return False

    def set_attribute_basic(self, key, value, depth):
        self.key = key
        self.value = value
        self.depth = depth

    def set_attribute_flag(self, first_flag, last_flag):
        self.is_first = first_flag
        self.is_last = last_flag

    def set_attribute_append(self, icon):
        self.icon = icon

    @abstractmethod
    def draw(self) -> None:
        pass


class ContainerNode(Node):

    def __init__(self) -> None:
        self.node_children: List[Node] = []

    def add(self, node: Node) -> None:
        self.node_children.append(node)
        node.parent = self

    def remove(self, node: Node) -> None:
        self.node_children.remove(node)
        node.parent = None

    def is_container(self) -> bool:
        return True

    def draw(self, style_factory) -> None:
        context = strategy.Context(strategy.ContainerStrategy())
        context.operation(style_factory, self)


class LeafNode(Node):

    def draw(self, style_factory) -> None:
        context = strategy.Context(strategy.LeafStrategy())
        context.operation(style_factory, self)
