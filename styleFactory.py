from abc import ABC, abstractmethod
from iconFactory import AbstractIconFactory


class AbstractStyleFactory(ABC):

    @abstractmethod
    def render_container_node(self, icon):
        pass

    @abstractmethod
    def render_leaf_node(self, icon):
        pass


"""Tree"""


class TreeStyleFactory(AbstractStyleFactory):

    def render_container_node(self, node):
        prefix = ""
        nest_depth = []
        pre_node = node
        while True:

            if pre_node.is_last is False:
                nest_depth.append(pre_node.depth)

            if pre_node.depth == 0:
                break
            pre_node = pre_node.node_parent

        for i in range(node.depth):
            if i in nest_depth:
                prefix += "│ "
            else:
                prefix += "  "

        if node.is_last is True:
            prefix += "└─"

        else:
            prefix = "├─"

        prefix += f"{node.icon} {node.key}"
        print(prefix)

    def render_leaf_node(self, node):
        prefix = ""
        pre_node = node.node_parent
        nest_depth = []

        while True:
            if pre_node.is_last is False:
                nest_depth.append(pre_node.depth)
            if pre_node.depth == 0:
                break
            pre_node = pre_node.node_parent

        for i in range(node.depth):
            if i in nest_depth:
                prefix += "│ "
            else:
                prefix += "  "

        if node.is_last is True:
            prefix += "└─"
        else:
            prefix += "├─"

        prefix += f"{node.icon} {node.key}:{node.value}"
        print(prefix)


"""Rectangle"""
MAX_LENGTH = 50


class RectangleStyleFactory(AbstractStyleFactory):

    def render_container_node(self, node):
        prefix = ""
        pre_node = node
        end_flag = True
        while True:
            if pre_node.is_last is False:
                end_flag = False
            if pre_node.depth == 0:
                break
            pre_node = pre_node.node_parent

        if end_flag is False:
            for i in range(node.depth):
                prefix += "│ "
        else:
            for i in range(node.depth):
                prefix += "└─"

        if node.depth == 0:
            if node.is_first is True:
                prefix += "┌─"

            if node.is_first is False:
                prefix += "├─"

        else:
            prefix += "├─"

        prefix += f"{node.icon} {node.key} "
        length = len(prefix)
        while length < MAX_LENGTH:
            prefix += "─"
            length += 1
        if node.depth == 0 and node.is_first is True:
            prefix += "─┐"
        else:
            prefix += "─┤"
        print(prefix)

    def render_leaf_node(self, node):
        prefix = ""
        pre_node = node
        end_flag = True
        while True:
            if pre_node.is_last is False:
                end_flag = False
            if pre_node.depth == 0:
                break
            pre_node = pre_node.node_parent

        if end_flag is False:
            for i in range(node.depth):
                prefix += "│ "
            prefix += "├─"
        else:
            for i in range(node.depth):
                prefix += "└─"
            prefix += "└─"

        prefix += f"{node.icon} {node.key}:{node.value} "
        length = len(prefix)
        while length < MAX_LENGTH:
            prefix += "─"
            length += 1

        if end_flag is True:
            prefix += "─┘"
        else:
            if node.depth == 0 and node.is_first is True:
                prefix += "─┐"
            else:
                prefix += "─┤"
        print(prefix)
