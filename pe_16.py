num = str(2**1000)
digit_sum = 0

for i in range(len(num)):
	digit_sum += int(num[i])

print(digit_sum)
