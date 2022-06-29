
def get_digit_sum(n):
	digit_sum = 0

	while n > 0:
		digit_sum += n % 10
		n //= 10

	return digit_sum


def is_digit_power_sum(n, digit_sum):

	if digit_sum == 1:
		return False

	if n < 100:
		return False

	p = 2
	while digit_sum**p < n:
		p += 1

	return digit_sum**p == n


members_set = set()
digit_power_set = set()
elements_n = 0

for a in range(2, 201):
	for b in range(2, 101):
		val = a**b
		if val < 10**15:
			digit_sum = get_digit_sum(val)
			if is_digit_power_sum(val, digit_sum):
				members_set.add(val)

members_set = sorted(members_set)

for member in members_set:
	if is_digit_power_sum(member, get_digit_sum(member)):
		elements_n += 1
		digit_power_set.add(member)

	if elements_n == 30:
		break

print(members_set)