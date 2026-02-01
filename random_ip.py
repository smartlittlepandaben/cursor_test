import random
a = str(random.randrange(1, 255))
b = str(random.randrange(0, 255))
c = str(random.randrange(0, 255))
d = str(random.randrange(0, 255))
ip = a + '.' + b + '.' + c + '.' + d
print('随机IP地址是：', ip)
