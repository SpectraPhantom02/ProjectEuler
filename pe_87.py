
import copy

# 7069 - largest prime whose square is below 50,000,000 - 908th prime
# 367 - largest prime whose cube is below 50,000,000 - 73rd prime
# 83 - largest prime whose fourth power is below 50,000,000 - 23rd prime


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


sums_set = set()
prime_sieve = Sieve(7070)
primes_list = prime_sieve.get_primes_list()

square_primes = copy.copy(primes_list)
cube_primes = [prime for prime in primes_list if prime <= 367]
fourth_power_primes = [prime for prime in primes_list if prime <= 83]

for p2 in square_primes:
	for p3 in cube_primes:

		if p2**2 + p3**3 >= 50000000:
			break

		for p4 in fourth_power_primes:

			if p2**2 + p3**3 + p4**4 >= 50000000:
				break

			sums_set.add(p2**2 + p3**3 + p4**4)

print(len(sums_set))