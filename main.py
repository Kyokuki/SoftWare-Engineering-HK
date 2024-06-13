import argparse
import json
from explorer import FunnyJsonExplorer


def main():

    # 指令解析
    parser = argparse.ArgumentParser(description="Funny JSON Explorer (FJE)")
    parser.add_argument('-f', '--file', type=str, default="D:/个人/软件工程/Funny_JSON_Explorer/json/fruit.json",
                        help="JSON file path")
    parser.add_argument('-s', '--style', type=str, choices=['tree', 'rectangle'], default='tree',
                        help="Style: 'tree' or 'rectangle'")
    parser.add_argument('-i', '--icon', type=str, choices=['poker', 'chess'], default='poker',
                        help="Icon family: 'family1' or 'family2'")
    args = parser.parse_args()

    # 读取JSON文件
    with open(args.file) as file:
        json_data = json.load(file)

    # 构建FJE，并实现可视化
    explorer = FunnyJsonExplorer(args.style, args.icon, json_data)
    explorer.build()
    explorer.show()


if __name__ == '__main__':
    main()

