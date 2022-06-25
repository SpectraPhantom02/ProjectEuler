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

def is_left_trunc_prime(n):
	if n < 10:
		return False

	n_digits = int(math.log10(n) + 1)
	while is_prime(n):
		divisor = 10 ** n_digits
		n %= divisor
		n_digits -= 1

	return n == 0


def is_right_trunc_prime(n):
	if n < 10:
		return False

	while is_prime(n):
		n //= 10

	return n == 0



sieve_obj = Sieve(739398)
primes_list = sieve_obj.get_primes_list()
truncatable_primes = []


for prime in primes_list:
	if is_left_trunc_prime(prime) and is_right_trunc_prime(prime):
		truncatable_primes.append(prime)

print(sum(truncatable_primes))