# 任务：输入三个整数x,y,z，请把这三个数由小到大输出。

L = []
for i in range(3):
    x = int(input('请分别三次各输入一个整数：'))
    L.append(x)
L.sort()
print('这组整数是：', L)
