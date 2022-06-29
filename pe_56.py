 
def get_sum_of_digits(n):
 	sum_digits = 0

 	while n > 0:
 		sum_digits += (n % 10)
 		n //= 10

 	return sum_digits


highest_digits_count = 0
highest_digit_base = 0
highest_digits_exponent = 0
for a in range(2, 100):
	for b in range(2, 100):
		val = a ** b
		sum_digits = get_sum_of_digits(val)
		if sum_digits > highest_digits_count:
			highest_digits_count = sum_digits
			highest_digit_base, highest_digits_exponent = a, b

print(f"Base/Exponent with most digits: {highest_digit_base}^{highest_digits_exponent}")
print(f"Number of digits: {highest_digits_count}")