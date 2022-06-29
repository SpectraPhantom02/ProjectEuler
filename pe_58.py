import math


def is_prime(n):
	if n < 2:
		return False

	for i in range(2, int(math.sqrt(n) + 1)):
		if not n % i:
			return False

	return True


primes_count = 3
total_count = 5

current_num = 9
spiral_side_length = 4

while primes_count / total_count >= 0.1:
	current_round_nums = [current_num + 1 * spiral_side_length,
	                      current_num + 2 * spiral_side_length,
	                      current_num + 3 * spiral_side_length,
	                      current_num + 4 * spiral_side_length]

	for num in current_round_nums:
		if is_prime(num):
			primes_count += 1
		total_count += 1
		

	current_num += (4 * spiral_side_length)
	spiral_side_length += 2


print(spiral_side_length - 2)