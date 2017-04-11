# 任务：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

s = input('请输入一行字符：')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('''char = %d
space = %d
digit = %d
others = %d''' % (letters, space, digit, others))

# 输出结果

请输入一行字符：py1 th2 on3 ,.
char = 6
space = 3
digit = 3
others = 2
