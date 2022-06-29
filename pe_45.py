
def get_triangular_number(n):
	return n*(n - 1) // 2

def get_pentagonal_number(n):
	return n*(3*n - 1) // 2

def get_hexagonal_number(n):
	return n*(2*n - 1)


triangular_nums = []
pentagonal_nums = []
hexagonal_nums = []

i= 1
tier = 0
while True:

	curr_triangular_num = get_triangular_number(i)
	curr_pentagonal_num = get_pentagonal_number(i)
	curr_hexagonal_num = get_hexagonal_number(i)

	triangular_nums.append(curr_triangular_num)
	pentagonal_nums.append(curr_pentagonal_num)
	hexagonal_nums.append(curr_hexagonal_num)

	if curr_triangular_num in pentagonal_nums and curr_triangular_num in hexagonal_nums:
		print(curr_triangular_num)
		if tier > 1:
			break

		tier += 1

	i += 1
