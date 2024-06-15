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

<img src="assets/mode_factory.png" alt="抽象工厂">

### 组合模式

<img src="assets/mode_composite.png" alt="组合模式">

### 建造者模式

<img src="assets/mode_builder.png" alt="建造者模式">

### 迭代器模式

<img src="assets/mode_iterator.png" alt="迭代器模式">

### 策略模式

<img src="assets/mode_strategy.png" alt="策略模式">


