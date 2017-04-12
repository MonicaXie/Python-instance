# 任务：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个，
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。
# 到第十天早上想再吃时，见只剩下一个桃子了。
# 求第一天共摘了多少。

# 方法一：

n = 1
for i in range(9, 0, -1):
    n = (n + 1) * 2
print('第一天共摘了%d个桃子' % n)

# 方法二：

def num(day = 1):
    if not isinstance(day, int) or day > 10 or day <= 0:
        return -1
    elif day == 10:
        return 1
    else:
        return (num(day + 1) + 1) * 2
print('第一天共摘了%d个桃子' % num())

# 输出结果

第一天共摘了1534个桃子
