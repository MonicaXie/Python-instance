# 任务：有1对兔子，从出生后第3个月起，每个月都生1对兔子；
# 小兔子长到第3个月后，每个月又生1对兔子。
# 假如兔子都不死，问每个月的兔子总数为多少？

f1 = 1
f2 = 1
for i in range(1, 22):
    print('%10d %10d' % (f1, f2), end = '')
    if (i % 3) == 0:
        print()
    f1 = f1 + f2
    f2 = f1 + f2
    
# 输出结果
    
         1          1         2          3         5          8
        13         21        34         55        89        144
       233        377       610        987      1597       2584
      4181       6765     10946      17711     28657      46368
     75025     121393    196418     317811    514229     832040
   1346269    2178309   3524578    5702887   9227465   14930352
  24157817   39088169  63245986  102334155 165580141  267914296
