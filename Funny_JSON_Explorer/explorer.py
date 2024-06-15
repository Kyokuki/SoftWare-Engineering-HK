import style
import icon
import node
import iterator


class FunnyJsonExplorer:

    def __init__(self, my_style, my_icon, my_data):
        self.explorer_style = my_style
        self.explorer_icon = my_icon
        self.explorer_data = my_data
        self.style_factory = None
        self.icon_factory = None
        self.explorer_root = node.ContainerNode()
        self.explorer_collection = iterator.NodeCollection()

    # 设置 Style 工厂
    def set_style_factory(self):
        if self.explorer_style == "tree":
            self.style_factory = style.TreeStyleFactory
        elif self.explorer_style == "rectangle":
            self.style_factory = style.RectangleStyleFactory

    # 设置 Icon 工厂
    def set_icon_factory(self):
        if self.explorer_icon == "poker":
            self.icon_factory = icon.PokerIconFactory
        elif self.explorer_icon == "chess":
            self.icon_factory = icon.ChessIconFactory

    def build(self):
        self.set_style_factory()
        self.set_icon_factory()
        container_icon = self.icon_factory.create_container_icon(None)
        leaf_icon = self.icon_factory.create_leaf_icon(None)
        node_index = 0

        def traverse(data, parent_node, depth=0):
            nonlocal node_index
            if isinstance(data, dict):
                for index, (key, value) in enumerate(data.items()):

                    first_flag = (index == 0)
                    last_flag = (index == len(data) - 1)

                    # Container 节点
                    if isinstance(value, (dict, list)):
                        current_node = node.ContainerNode()
                        current_node.set_attribute_basic(key, value, depth)
                        current_node.set_attribute_flag(first_flag, last_flag)
                        current_node.set_attribute_append(container_icon)
                        self.explorer_collection.add_item(current_node)
                        traverse(value, current_node, depth + 1)
                        parent_node.add(current_node)

                    # Leaf 节点
                    else:
                        current_node = node.LeafNode()
                        current_node.set_attribute_basic(key, value, depth)
                        current_node.set_attribute_flag(first_flag, last_flag)
                        current_node.set_attribute_append(leaf_icon)
                        self.explorer_collection.add_item(current_node)
                        parent_node.add(current_node)

        traverse(self.explorer_data, self.explorer_root, 0)

    def show(self):
        print(f"\n********** Funny Json Explorer **********\n"
              f"style -- {self.explorer_style}        icon -- {self.explorer_icon}\n")
        for item in self.explorer_collection:
            item.draw(self.style_factory)
