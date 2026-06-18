实验：按钮控制LED模式切换

目标

按按钮切换LED模式。

0 -> 灭

1 -> 常亮

2 -> 闪烁

---

使用组件

- Button
- Led

---

实现逻辑

按钮按下：

mode += 1

超过2：

mode = 0

根据mode执行：

mode=0:
led.off()

mode=1:
led.on()

mode=2:
led.blink()

---

遇到的问题

最初把：

mode判断

写成了：

elif

导致按钮按下时LED逻辑不执行。

修改为：

两个独立if逻辑。

---

结果

成功理解：

输入 -> 决策 -> 输出

的基本机器人结构。
---

3. code（建议保存）

把今天最终版本代码保存。

例如：

robotlab/code/button_led_mode.py

里面放今天最终整理版代码。

以后你会发现：

experiment
记录做过什么

code
保存最终代码

两个用途不一样。