
LIMIT = 10000

def is_palindrome(n):
	return str(n) == str(n)[::-1]

def get_mirror_number(n):
	return int(str(n)[::-1])


lychrel_numbers_count = 0
for i in range(1, LIMIT + 1):
	n_iters = 0
	total = i
	while n_iters < 50:
		total += get_mirror_number(total)
		if is_palindrome(total):
			break

		if n_iters == 49:
			lychrel_numbers_count += 1

		n_iters += 1

print(lychrel_numbers_count)