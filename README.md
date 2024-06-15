# Funny JSON Explorer

## 使用方法

在 conda 环境下，进入代码文件并在命令行执行：

`python main.py -f <file> -s <style> -i <icon>`

`<file>` 为JSON文件的路径。

`<style>` 为渲染风格，目前支持 `tree` 和 `rectangle`。

`<icon>` 为渲染图标族，目前支持 `poker` 和 `chess`。

## 输出展示

<img src="assets/result_rectangle_chess.png" alt="结果图：矩形棋盘" width="400"> <img src="assets/result_rectangle_poker.png" alt="结果图：矩形扑克" width="400">



<img src="assets/result_tree_chess.png" alt="结果图：树状棋盘" width="400"> <img src="assets/result_tree_poker.png" alt="结果图：树状扑克" width="400">

## UML类图

<img src="assets/UML.png" alt="UML类图" width="800">

## 设计模式

### 抽象工厂

<img src="assets/mode_factory.png" alt="抽象工厂" width="400">

**抽象工厂模式**通过解析指令，判断指令中指定的渲染风格以及图标族，并返回对应的渲染风格和图标族。

### 组合模式

<img src="assets/mode_composite.png" alt="组合模式" width="400">

**组合模式**可以将各个节点构建为树状嵌套递归对象结构，且各个节点仍可以当作独立对象进行调用。

### 建造者模式

<img src="assets/mode_builder.png" alt="建造者模式" width="400">

此处的**建造者模式**并未通过定义一个新的类实现，而是直接在 `Node` 类中进行实现。由于构建一个节点需要经过多个步骤，因此我们将这些步骤换成依次调用的 `set_attribute_<···>` 方法。

### 迭代器模式

<img src="assets/mode_iterator.png" alt="迭代器模式" width="400">

**迭代器模式**可以让我们能够通过遍历的方式依次访问树状结构中的各个节点。

### 策略模式

<img src="assets/mode_strategy.png" alt="策略模式" width="400">

对于树状结构中的叶子节点和容器节点，我们对其渲染策略并不相同，因此我们通过**策略模式**在渲染节点时根据节点类型调整渲染策略。


