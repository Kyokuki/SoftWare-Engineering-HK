from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, style, icon):
        self.style = style
        self.icon = icon

    @abstractmethod
    def draw(self, indent=0):
        pass

class Container(Component):
    def __init__(self, name, level, style, icon):
        super().__init__(style, icon)
        self.name = name
        self.level = level
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def draw(self, indent="", is_last=True, first_call=True):
        icon = ' '
        if self.icon == 'poker-face':
            icon = '♠'
        elif self.icon == 'star':
            icon = '✪'

        if self.style == 'tree':
            print(f"{indent}{'└─ ' if is_last else '├─ '}{icon} {self.name}")
            indent += "    " if is_last else "|   "
        elif self.style == 'rectangle':
            if first_call:
                print(f"{indent}┌─ {icon} {self.name} {'─' * (27 - len(indent) - len(self.name) - 2)}┐")
            else:
                connector = '└──' if is_last else '├─ '
                print(
                    f"{indent}{connector}{icon} {self.name} {'─' * (30 - len(indent) - len(self.name) - len(connector) - 2)}┤" if not is_last else f"{indent}{connector}{icon} {self.name} {'─' * (30 - len(indent) - len(self.name) - len(connector) - 2)}┘")
            if not first_call:
                indent += "────" if is_last else "└── "
            else:
                indent += "└───"

        for i, child in enumerate(self.children):
            is_last_child = i == len(self.children) - 1
            child.draw(indent, is_last_child, first_call=False)


class Leaf(Component):
    def __init__(self, name, style, icon):
        super().__init__(style, icon)
        self.name = name

    def draw(self, indent="", is_last=True, first_call=False):
        icon = ''
        if self.icon == 'poker-face':
            icon = '♣'
        elif self.icon == 'star':
            icon = '✩'

        if self.style == 'tree':
            print(f"{indent}{'└─ ' if is_last else '├─ '}{icon} {self.name}")
        elif self.style == 'rectangle':
            connector = '└─ ' if is_last else '├─ '
            print(
                f"{indent}{connector}{icon} {self.name} {'─' * (30 - len(indent) - len(self.name) - len(connector) - 2)}┤" if not is_last else f"{indent}{connector}{icon} {self.name} {'─' * (30 - len(indent) - len(self.name) - len(connector) - 2)}┘")
