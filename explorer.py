import styleFactory
import iconFactory
import node


class FunnyJsonExplorer:

    def __init__(self, style, icon, data):
        self.explorer_style = style
        self.explorer_icon = icon
        self.explorer_data = data
        self.style_factory = None
        self.icon_factory = None
        self.root = node.ContainerNode()

    # 设置 Style 工厂
    def set_style_factory(self):
        if self.explorer_style == "tree":
            self.style_factory = styleFactory.TreeStyleFactory
        elif self.explorer_style == "rectangle":
            self.style_factory = styleFactory.RectangleStyleFactory

    # 设置 Icon 工厂
    def set_icon_factory(self):
        if self.explorer_icon == "poker":
            self.icon_factory = iconFactory.PokerIconFactory
        elif self.explorer_icon == "music":
            self.icon_factory = iconFactory.MusicIconFactory

    def build(self):
        self.set_style_factory()
        self.set_icon_factory()
        container_icon = self.icon_factory.create_container_icon(None)
        leaf_icon = self.icon_factory.create_leaf_icon(None)

        def traverse(data, parent_node, depth=0):
            if isinstance(data, dict):
                for index, (key, value) in enumerate(data.items()):

                    first_flag = (index == 0)
                    last_flag = (index == len(data) - 1)

                    # Container 节点
                    if isinstance(value, (dict, list)):
                        current_node = node.ContainerNode()
                        current_node.key = key
                        current_node.depth = depth
                        current_node.is_first = first_flag
                        current_node.is_last = last_flag
                        current_node.icon = container_icon
                        traverse(value, current_node, depth + 1)
                        parent_node.add(current_node)

                    # Leaf 节点
                    else:
                        current_node = node.LeafNode()
                        current_node.key = key
                        current_node.value = value
                        current_node.depth = depth
                        current_node.is_first = first_flag
                        current_node.is_last = last_flag
                        current_node.icon = leaf_icon
                        parent_node.add(current_node)

        traverse(self.explorer_data, self.root, 0)

    def show(self):
        print(f"\n✦ Funny Json Explorer :  style -- {self.explorer_style}  icon -- {self.explorer_icon}\n")
        for child in self.root.node_children:
            child.draw(self.style_factory)
