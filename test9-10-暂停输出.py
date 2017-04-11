# 任务：暂停一秒输出。

import time
myD = {'Liuz': 32, 'Monica': 31}
for key, value in dict.items(myD):
	print(key, value)
	time.sleep(1) # 暂停1秒

# 任务：暂停一秒输出，并格式化当前时间。

import time
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(1) # 暂停1秒
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
