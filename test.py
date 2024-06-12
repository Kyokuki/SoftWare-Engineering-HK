import json

# 工厂方法模式
class JSONExplorerFactory:
    def create_explorer(self, style):
        if style == 'tree':
            return TreeJSONExplorer()
        elif style == 'rectangle':
            return RectangleJSONExplorer()
        else:
            raise ValueError(f"Unsupported style: {style}")

# 抽象工厂模式
class JSONIconFactory:
    def create_icon(self, icon_family):
        if icon_family == 'family1':
            return "[+]"
        elif icon_family == 'family2':
            return "[*]"
        else:
            raise ValueError(f"Unsupported icon family: {icon_family}")

# 建造者模式
class JSONExplorerBuilder:
    def __init__(self):
        self.explorer = None

    def set_style(self, style):
        if style == 'tree':
            self.explorer = TreeJSONExplorer()
        elif style == 'rectangle':
            self.explorer = RectangleJSONExplorer()
        else:
            raise ValueError(f"Unsupported style: {style}")

    def set_icon_family(self, icon_family):
        if self.explorer is None:
            raise ValueError("Style must be set before setting icon family")
        icon_factory = JSONIconFactory()
        icon = icon_factory.create_icon(icon_family)
        self.explorer.set_icon(icon)

    def get_explorer(self):
        if self.explorer is None:
            raise ValueError("Style and icon family must be set before getting explorer")
        return self.explorer

# 组合模式
class JSONExplorerComponent:
    def __init__(self):
        self.icon = None

    def set_icon(self, icon):
        self.icon = icon

    def render(self):
        raise NotImplementedError()

class JSONExplorerLeaf(JSONExplorerComponent):
    def __init__(self, key, value):
        super().__init__()
        self.key = key
        self.value = value

    def render(self):
        icon_str = self.icon.get_icon_str() if self.icon else ''
        return f"{icon_str} {self.key}: {self.value}"

class JSONExplorerComposite(JSONExplorerComponent):
    def __init__(self, key):
        super().__init__()
        self.key = key
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def render(self):
        icon_str = self.icon.get_icon_str() if self.icon else ''
        result = f"{icon_str} {self.key}:\n"
        for child in self.children:
            result += f"  {child.render()}\n"
        return result


# 具体组件类
class Family1Icon:

    def get_icon_str(self):

        return "[class Family2Icon:"

    def get_icon_str(self):

        return "{"


# 具体构建者类
class TreeJSONExplorer:
    def __init__(self):
        self.root = None

    def set_icon(self, icon):
        self.icon = icon

    def build(self, data):
        self.root = self._build_tree(data)

    def _build_tree(self, data):
        if isinstance(data, dict):
            composite = JSONExplorerComposite("")
            for key, value in data.items():
                child = self._build_tree(value)
                composite.add_child(JSONExplorerLeaf(key, child))
            return composite
        elif isinstance(data, list):
            composite = JSONExplorerComposite("")
            for index, item in enumerate(data):
                child = self._build_tree(item)
                composite.add_child(JSONExplorerLeaf(str(index), child))
            return composite
        else:
            return JSONExplorerLeaf("", str(data))

    def render(self):
        if self.root:
            return self.root.render()
        else:
            return ""


class RectangleJSONExplorer:
    def __init__(self):
        self.data = None

    def set_icon(self, icon):
        self.icon = icon

    def build(self, data):
        self.data = data

    def render(self):
        if self.data:
            return json.dumps(self.data, indent=2)
        else:
            return ""

# 客户端代码
def main():
    import argparse

    parser = argparse.ArgumentParser(description="Funny JSON Explorer (FJE)")
    parser.add_argument('-f', '--file', type=str, default="D:/个人/软件工程/Funny_JSON_Explorer/json/fruit.json",
                        help="JSON file path")
    parser.add_argument('-s', '--style', type=str, choices=['tree', 'rectangle'], default='tree',
                        help="Style: 'tree' or 'rectangle'")
    parser.add_argument('-i', '--icon', type=str, choices=['family1', 'family2'], default='family1',
                        help="Icon family: 'family1' or 'family2'")

    args = parser.parse_args()

    # 读取JSON文件
    with open(args.file) as file:
        json_data = json.load(file)

    # 使用建造者模式构建Explorer
    builder = JSONExplorerBuilder()
    builder.set_style(args.style)
    builder.set_icon_family(args.icon)
    explorer = builder.get_explorer()
    explorer.build(json_data)

    # 渲染并输出结果
    print(explorer.render())

if __name__ == "__main__":
    # print(
    # "├─♦oranges\n" +
    # "|  └─♦mandarin\n" +
    # "|     ├─♠clementine\n" +
    # "|     └─♠tangerine:cheap & juicy!\n" +
    # "└─♦apples\n" +
    # "   ├─♠gala\n" +
    # "   └─♠pink lady\n")

    # print(
    # "├─♫oranges\n" +
    # "|  └─♫mandarin\n" +
    # "|     ├─♪clementine\n" +
    # "|     └─♪tangerine:cheap & juicy!\n" +
    # "└─♫apples\n" +
    # "   ├─♪gala\n" +
    # "   └─♪pink lady\n")

    # print(
    # "┌─♦oranges───────────────────────────────────────┐\n" +
    # "|──├─♦mandarin───────────────────────────────────|\n" +
    # "|──|──├─♠clementine──────────────────────────────|\n" +
    # "|──|──├─♠tangerine:cheap & juicy!────────────────|\n" +
    # "├─♦apples────────────────────────────────────────|\n" +
    # "|──├─♠gala───────────────────────────────────────|\n" +
    # "└──└─♠pink lady──────────────────────────────────┘\n")

    print(
    "┌─♫oranges───────────────────────────────────────┐\n" +
    "|──├─♫mandarin───────────────────────────────────|\n" +
    "|──|──├─♪clementine──────────────────────────────|\n" +
    "|──|──├─♪tangerine:cheap & juicy!────────────────|\n" +
    "├─♫apples────────────────────────────────────────|\n" +
    "|──├─♪gala───────────────────────────────────────|\n" +
    "└──└─♪pink lady──────────────────────────────────┘\n")