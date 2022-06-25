
LIMIT = 20000000

sieve = [i for i in range(LIMIT)] 
sieve[1] = 0

def calculate_prime_sum(sieve, limit):
	prime_sum = 0
	index = 2
	while index < limit:
		prime_sum += index
		for i in range(index, LIMIT, index):
			sieve[i] = 0
		index = get_next_sieve_prime(sieve, index, limit)

	return prime_sum

def get_next_sieve_prime(sieve, start, limit):
	index = start 
	while True:
		if index >= limit:
			return limit

		if sieve[index] != 0:
			return index
		index += 1

prime_sum = calculate_prime_sum(sieve, LIMIT)
print(prime_sum)