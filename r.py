import random

r = random.randint(1, 100)
count = 0

while True:
	count += 1 #count = count + 1
	num = input('請猜數字')
	num = int(num)
	if num == r:
		print('你猜對了')
		print('你猜了', count, '次後答對')
		break
	elif num > r:
		print('比數字大')
	elif num < r:
		print('比數字小')
	print('這是你猜的第', count, '次')
