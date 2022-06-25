import math


class Sieve:

	def __init__(self, limit):
		self.limit = limit
		self.sieve = [i for i in range(limit)] 
		self.sieve[1] = 0
		self.primes_list = []

	def get_sieve(self):
		index = 2
		while index < self.limit:
			self.primes_list.append(index)
			for i in range(index, self.limit, index):
				self.sieve[i] = 0

			index = self.get_next_sieve_prime(index)

		return self.sieve

	def get_next_sieve_prime(self, start):
		index = start 
		while True:
			if index >= self.limit:
				return self.limit

			if self.sieve[index] != 0:
				return index
			index += 1

	def get_primes_list(self):
		self.prime_sieve = self.get_sieve()
		return self.primes_list


def is_prime(n):
	if n < 2:
		return False

	for i in range(2, int(math.sqrt(n) + 1)):
		if not n % i:
			return False

	return True

def is_circular_prime(n):
	total_digits = int(math.log10(n) + 1)
	digits = total_digits

	while digits > 0:
		last_digit = n % 10
		n = (last_digit * (10**(total_digits)) + n) // 10
		if not is_prime(n):
			return False
		digits -= 1

	return True


sieve_obj = Sieve(10**6)
primes_list = sieve_obj.get_primes_list()
circular_primes = []

for prime in primes_list:
	if is_circular_prime(prime):
		circular_primes.append(prime)


print(len(circular_primes))