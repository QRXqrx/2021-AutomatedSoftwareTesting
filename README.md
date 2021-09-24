## 说明

该仓库包含NJU自动化测试2021源码分析方向部分题目所需的实验对象。

实验对象包括两大类：

1. 面向对象SUT（BPlusTree ~ Sudoku）
2. 符号执行小程序（xx-examples）。

:construction:python符号执行小程序还未编写完成；预期是和java小程序逻辑类似的python版本



#### Tips

1. 面向对象SUT均通过Maven构建。src/java目录下为待测逻辑，src/test下测试代码表示”已存在的测试数据（Exisiting Test Data）“，测试再生成和Seeding就在这些给定测试数据的基础上完成。
2. 可以在不改变小程序基本逻辑的前提下进行适当修改。比如：修改程序以匹配自身实现的输入要求、修改程序的Test Driver部分以满足某些需求等。



#### 联系方式

- qrx@smail.nju.edu.cn

