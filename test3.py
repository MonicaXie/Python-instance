# 任务：一个整数在10000以内，它加上100和加上268后都是一个完全平方数，请问该数是多少？

import math
for i in range(10000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if (x * x == i + 100) and (y * y == i + 268):
        print(i)

# 输出结果：
21
261
1581
