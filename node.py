from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from styleFactory import AbstractStyleFactory


class Node(ABC):

    def __init__(self):
        self.key = None
        self.value = None
        self.icon = None
        self.depth = 0
        self.is_first = False
        self.is_last = False
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

    def draw(self, style_factory: AbstractStyleFactory) -> None:
        style_factory.render_container_node(self, self)
        for child in self.node_children:
            child.draw(style_factory)


class LeafNode(Node):

    def draw(self, style_factory: AbstractStyleFactory) -> None:
        style_factory.render_leaf_node(self, self)
