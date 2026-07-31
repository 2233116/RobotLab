# 状态(State)与事件(Event)

状态：

表示当前系统处于某种模式。

例如：

mode = 0
mode = 1
mode = 2

特点：

持续存在。

例：

if mode == 1:
    buzzer.on()

--------------------------------

事件(Event)

表示某个动作发生了一次。

例如：

button.is_pressed()

特点：

瞬时发生。

例：

if button.is_pressed():
    buzzer.beep()

--------------------------------

原则

持续行为放状态。

一次性行为放事件。

以后超声波避障、PID控制、ROS2状态机都会大量使用该思想。